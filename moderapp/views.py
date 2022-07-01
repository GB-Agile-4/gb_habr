from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from articleapp.models import Article
from authapp.models import HabrUser


def ban_user(request, pk):

    habr_user = HabrUser.objects.filter(pk=pk).first()

    if habr_user.is_banned:
        habr_user.is_banned = False
    else:
        habr_user.is_banned = True
    habr_user.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def moderate_list(request):
    articles = Article.objects.filter(is_moderated=False, reject_moderation=False)

    context = {
        'articles': articles,
    }

    return render(request, 'moderapp/moder_list.html', context=context)


def moderate_post(request, pk):
    article = Article.objects.filter(pk=pk).first()

    context = {
        'article': article,
    }

    return render(request, 'moderapp/moderate_post.html', context=context)


def confirm_moderate_post(request, pk):
    article = Article.objects.filter(pk=pk).first()

    article.is_moderated = True
    article.save()

    return HttpResponseRedirect(reverse('moderapp:moderate_list'))


def reject_moderate_post(request, pk):
    article = Article.objects.filter(pk=pk).first()

    article.reject_moderation = True
    article.save()

    return HttpResponseRedirect(reverse('moderapp:moderate_list'))