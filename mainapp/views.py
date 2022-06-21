from django.shortcuts import render
from django.shortcuts import get_object_or_404

from articleapp.models import ArticleCategory, Article


def index(request):
    article_categories = ArticleCategory.objects.all()
    articles = Article.objects.all()

    context = {
        'article_categories': article_categories,
        'articles': articles
    }

    return render(request, 'mainapp/index.html', context=context)


def articles(request, pk):
    article_categories = ArticleCategory.objects.all()

    if pk == 0:
        articles = Article.objects.all()
        category_item = {'name': 'Все потоки',
                         'pk': 0}
    else:
        category_item = get_object_or_404(ArticleCategory, pk=pk)
        articles = Article.objects.filter(category__pk=pk)

    context = {
        'article_categories': article_categories,
        'category_item': category_item,
        'articles': articles
    }

    return render(request, 'mainapp/index.html', context=context)


def hubs(request):
    article_categories = ArticleCategory.objects.all()

    context = {
        'article_categories': article_categories
    }
    return render(request, 'mainapp/hubs.html', context=context)


def help(request):
    return render(request, 'mainapp/help.html')
