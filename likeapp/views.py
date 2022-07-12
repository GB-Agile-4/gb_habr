from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from notifications.signals import notify

from commentapp.models import Comment
from .models import Mark, CommentMark
from articleapp.models import Article


@login_required()
def add_like(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.user.is_authenticated and request.user != article.author:

        if request.user.is_banned:
            return HttpResponseRedirect(reverse('accountapp:account', args=[request.user.username]))

        user_mark = Mark.objects.filter(habruser=request.user, marked_article=article).first()

        if user_mark:
            if user_mark.mark == 'like':
                user_mark.delete()
                article.likes -= 1

            elif user_mark.mark == 'dislike':
                user_mark.delete()
                user_mark = Mark(habruser=request.user, marked_article=article, mark='like')
                user_mark.save()
                article.likes += 1

                notify.send(request.user, recipient=article.author, action_object=article, description='article',
                            verb=f'Ваша статья {article.title} понравилась пользователю {request.user.get_full_name()}.')

                article.dislikes -= 1
        else:
            user_mark = Mark(habruser=request.user, marked_article=article, mark='like')
            user_mark.save()
            article.likes += 1

            notify.send(request.user, recipient=article.author, action_object=article, description='article',
                        verb=f'Ваша статья {article.title} понравилась пользователю {request.user.get_full_name()}.')

        article.rating = article.likes - article.dislikes
        article.save()

    return HttpResponseRedirect(reverse('article:article_detail', args=(pk,)))


@login_required()
def add_dislike(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.user.is_authenticated and request.user != article.author:

        if request.user.is_banned:
            return HttpResponseRedirect(reverse('accountapp:account', args=[request.user.username]))

        user_mark = Mark.objects.filter(habruser=request.user, marked_article=article).first()

        if user_mark:
            if user_mark.mark == 'dislike':
                user_mark.delete()
                article.dislikes -= 1

            elif user_mark.mark == 'like':
                user_mark.delete()
                user_mark = Mark(habruser=request.user, marked_article=article, mark='dislike')
                user_mark.save()
                article.dislikes += 1
                article.likes -= 1
        else:
            user_mark = Mark(habruser=request.user, marked_article=article, mark='dislike')
            user_mark.save()
            article.dislikes += 1

        article.rating = article.likes - article.dislikes
        article.save()

    return HttpResponseRedirect(reverse('article:article_detail', args=(pk,)))


@login_required()
def comment_like(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user.is_authenticated and request.user != comment.comment_author:

        if request.user.is_banned:
            return HttpResponseRedirect(reverse('accountapp:account', args=[request.user.username]))

        user_mark = CommentMark.objects.filter(habruser=request.user, marked_comment=comment).first()

        if user_mark:
            if user_mark.mark == 'like':
                user_mark.delete()
                comment.likes -= 1
                comment.save()

            elif user_mark.mark == 'dislike':
                user_mark.delete()
                user_mark = CommentMark(habruser=request.user, marked_comment=comment, mark='like')
                user_mark.save()
                comment.likes += 1
                comment.dislikes -= 1
                comment.save()

                notify.send(request.user, recipient=comment.comment_author, action_object=comment.article, description='article',
                            verb=f'Ваш комментарий к статье {comment.article.title} понравился пользователю {request.user.get_full_name()}.')
        else:
            user_mark = CommentMark(habruser=request.user, marked_comment=comment, mark='like')
            user_mark.save()
            comment.likes += 1
            comment.save()

            notify.send(request.user, recipient=comment.comment_author, action_object=comment.article,
                        description='article',
                        verb=f'Ваш комментарий к статье {comment.article.title} понравился пользователю {request.user.get_full_name()}.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def comment_dislike(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user.is_authenticated and request.user != comment.comment_author:

        if request.user.is_banned:
            return HttpResponseRedirect(reverse('accountapp:account', args=[request.user.username]))

        user_mark = CommentMark.objects.filter(habruser=request.user, marked_comment=comment).first()

        if user_mark:
            if user_mark.mark == 'dislike':
                user_mark.delete()
                comment.dislikes -= 1
                comment.save()

            elif user_mark.mark == 'like':
                user_mark.delete()
                user_mark = CommentMark(habruser=request.user, marked_comment=comment, mark='dislike')
                user_mark.save()
                comment.dislikes += 1
                comment.likes -= 1
                comment.save()

        else:
            user_mark = CommentMark(habruser=request.user, marked_comment=comment, mark='dislike')
            user_mark.save()
            comment.dislikes += 1
            comment.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
