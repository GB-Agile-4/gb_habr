from django.shortcuts import render
from django.shortcuts import get_object_or_404

from articleapp.models import ArticleCategory, Article

import datetime


def top_articles():
    one_month = datetime.date.today() - datetime.timedelta(days=30)
    top_articles = Article.objects.filter(is_active=True,
                                          is_moderated=True,
                                          created_at__gt=one_month).order_by('-rating')[:5]
    return top_articles


def articles_read_now():
    seven_days = datetime.date.today() - datetime.timedelta(days=7)
    articles_read_now = Article.objects.filter(is_active=True,
                                               is_moderated=True,
                                               created_at__gt=seven_days).order_by('-views')[:5]

    print(seven_days, articles_read_now)
    return articles_read_now


def index(request):
    articles = Article.objects.filter(is_active=True, is_moderated=True).order_by('-created_at')

    context = {
        'articles': articles,
        'articles_read_now': articles_read_now(),
        'top_articles': top_articles()
    }

    return render(request, 'mainapp/index.html', context=context)


def articles(request, pk):

    if pk == 0:
        articles = Article.objects.filter(is_active=True, is_moderated=True).order_by('-created_at')
        category_item = {'name': 'Все потоки',
                         'pk': 0}
    else:
        category_item = get_object_or_404(ArticleCategory, pk=pk)
        articles = Article.objects.filter(is_active=True, is_moderated=True, category__pk=pk).order_by('-created_at')

    context = {
        'category_item': category_item,
        'articles': articles,
        'articles_read_now': articles_read_now(),
        'top_articles': top_articles()
    }

    return render(request, 'mainapp/index.html', context=context)


def help(request):
    context = {
        'articles_read_now': articles_read_now(),
        'top_articles': top_articles()
    }
    return render(request, 'mainapp/help.html', context)
