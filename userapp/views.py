from django.shortcuts import render
from authapp.models import HabrUser
from article.models import Article


def personal_area(request):

    articles = Article.objects.filter(author=request.user.pk)

    context = {
        'articles': articles
    }

    return render(request, 'userapp/personal_area.html', context=context)


def create_pub(request):

    return render(request, 'userapp/create_pub.html')

