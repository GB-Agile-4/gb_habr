from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from notifications.signals import notify

from articleapp.models import Article
from authapp.models import HabrUser
from commentapp.forms import CommentCreateForm
from commentapp.models import Comment


def comment_delete(request, pk):

    comment = Comment.objects.get(pk=pk)
    comment.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def add_comment(request, pk):
    template_name = 'commentapp/comment_form.html'
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        if request.user.is_banned:
            return HttpResponseRedirect(reverse('accountapp:account', args=[request.user.username]))
        comment_form = CommentCreateForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.comment_author = request.user
            new_comment.save()
            comment_form = CommentCreateForm()

            comment_text = new_comment.body
            if comment_text.startswith('@moderator'):
                notify.send(request.user, recipient=HabrUser.objects.filter(is_staff=True), action_object=article, description='article',
                            verb=f'Жалоба на статью {article.title} от пользователя {request.user.get_full_name()}.')

            notify.send(request.user, recipient=article.author, action_object=article, description='article',
                        verb=f'Вашей статье {article.title} оставил комментарий пользователь {request.user.get_full_name()}.')

    else:
        comment_form = CommentCreateForm()

    return render(request, template_name, {'article': article,
                                           'comment_form': comment_form})

@login_required()
def add_comment_reply(request, pk):
    template_name = 'commentapp/comment_form.html'
    comment = Comment.objects.get(pk=pk)
    article = comment.article

    if request.method == 'POST':
        if request.user.is_banned:
            return HttpResponseRedirect(reverse('accountapp:account', args=[request.user.username]))
        comment_form = CommentCreateForm(data=request.POST)
        if comment_form.is_valid():
            new_comment_reply = comment_form.save(commit=False)
            new_comment_reply.article = article
            new_comment_reply.parent = comment
            new_comment_reply.comment_author = request.user
            new_comment_reply.save()
            comment_form = CommentCreateForm()

            reply_text = new_comment_reply.body
            if reply_text.startswith('@moderator'):
                notify.send(request.user, recipient=HabrUser.objects.filter(is_staff=True), action_object=article,
                            description='article',
                            verb=f'Жалоба на комментарий к статье {article.title} от пользователя {request.user.get_full_name()}.')

            notify.send(request.user, recipient=article.author, action_object=article, description='article',
                        verb=f'На ваш комментарий к статье {article.title} оставил ответ пользователь {request.user.get_full_name()}.')

    else:
        comment_form = CommentCreateForm()

    return render(request, template_name, {'article': article,
                                           'comment_form': comment_form})
