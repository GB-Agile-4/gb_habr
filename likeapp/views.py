from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from commentapp.models import Comment
from .models import Mark, CommentMark
from articleapp.models import Article


def add_like(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.user.is_authenticated and request.user != article.author:
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
                article.dislikes -= 1
        else:
            user_mark = Mark(habruser=request.user, marked_article=article, mark='like')
            user_mark.save()
            article.likes += 1

        article.rating = article.likes - article.dislikes
        article.save()

    return HttpResponseRedirect(reverse('article:article_detail', args=(pk, )))


def add_dislike(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.user.is_authenticated and request.user != article.author:
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

    return HttpResponseRedirect(reverse('article:article_detail', args=(pk, )))


def comment_like(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user.is_authenticated and request.user != comment.comment_author:
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
        else:
            user_mark = CommentMark(habruser=request.user, marked_comment=comment, mark='like')
            user_mark.save()
            comment.likes += 1
            comment.save()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def comment_dislike(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user.is_authenticated and request.user != comment.comment_author:
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
