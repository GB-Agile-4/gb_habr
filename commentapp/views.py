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


# def add_comment(request, pk):
#     template_name = 'commentapp/comment_form.html'
#     article = get_object_or_404(Article, pk=pk)
#
#     if request.method == 'POST':
#         if request.user.is_banned:
#             return HttpResponseRedirect(reverse('accountapp:account', args=[request.user.username]))
#         comment_form = CommentCreateForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.article = article
#             new_comment.comment_author = request.user
#             new_comment.save()
#             comment_form = CommentCreateForm()
#
#     else:
#         comment_form = CommentCreateForm()
#
#     return render(request, template_name, {'article': article,
#                                            'comment_form': comment_form})

def add_comment(request, pk):
    template_name = 'commentapp/comment_form.html'
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.filter(is_active=True, parent__isnull=True)

    if request.method == 'POST':
        if request.user.is_banned:
            return HttpResponseRedirect(reverse('accountapp:account', args=[request.user.username]))
        comment_form = CommentCreateForm(data=request.POST)
        if comment_form.is_valid():
                parent_obj = None
                # get parent comment id from hidden input
                try:
                    # id integer e.g. 15
                    parent_id = int(request.POST.get('parent_id'))
                except:
                    parent_id = None
                # if parent_id has been submitted get parent_obj id
                if parent_id:
                    parent_obj = Comment.objects.get(id=parent_id)
                    # if parent object exist
                    if parent_obj:
                        # create replay comment object
                        replay_comment = comment_form.save(commit=False)
                        # assign parent_obj to replay comment
                        replay_comment.parent = parent_obj
                # normal comment
                # create comment object but do not save to database
                new_comment = comment_form.save(commit=False)
                # assign ship to the comment
                new_comment.article = article
                new_comment.comment_author = request.user
                # save
                new_comment.save()
                comment_form = CommentCreateForm()
                # return HttpResponseRedirect(article.get_absolute_url())
    else:
        comment_form = CommentCreateForm()

    # return render(request, template_name, {'article': article,
    #                                        'comment_form': comment_form})
    return render(request,
                  template_name,
                  {'article': article,
                   'comments': comments,
                   'comment_form': comment_form})
