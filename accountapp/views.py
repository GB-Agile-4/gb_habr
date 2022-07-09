from django.shortcuts import render

from articleapp.models import Article
from authapp.models import HabrUser


def personal_area(request, slug):
    articles = Article.objects.filter(author__username=slug)
    all_users = HabrUser.objects.all()
    habr_user = HabrUser.objects.get(username=slug)

    context = {
        'articles': articles,
        'all_users': all_users,
        'habr_user': habr_user
    }

    return render(request, 'accountapp/personal_area.html', context=context)
