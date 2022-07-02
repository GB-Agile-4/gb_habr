from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Mark
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
