from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from articleapp.models import Article
from commentapp.forms import CommentCreateForm
from commentapp.models import Comment


def comment_delete(request, pk):

    comment = Comment.objects.get(pk=pk)
    comment.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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

    else:
        comment_form = CommentCreateForm()

    return render(request, template_name, {'article': article,
                                           'comment_form': comment_form})
