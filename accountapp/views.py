from django.shortcuts import render
from datetime import datetime

from articleapp.models import Article
from authapp.models import HabrUser


def personal_area(request, slug):
    articles = Article.objects.filter(author__username=slug)
    habr_user = HabrUser.objects.get(username=slug)
    ban_expires = (habr_user.banned_till - datetime.now().date()).days

    context = {
        'articles': articles,
        'habr_user': habr_user,
        'ban_expires': ban_expires
    }

    return render(request, 'accountapp/personal_area.html', context=context)
