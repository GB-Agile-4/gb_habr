from django.shortcuts import render

from articleapp.models import Article
from authapp.models import HabrUser
from notificationapp.models import Notification


def personal_area(request, slug):
    articles = Article.objects.filter(author__username=slug)
    habr_user = HabrUser.objects.get(username=slug)
    notifications = Notification.objects.filter(article_author=habr_user).exclude(comment_author=habr_user)
    total_unread_number = notifications.count()
    articles_unread_number = {}

    for article in articles:
        if article.notifications:
            article_unread_number = notifications.filter(article=article).count()
        else:
            article_unread_number = 0
        articles_unread_number[article.id] = article_unread_number

    context = {
        'articles': articles,
        'habr_user': habr_user,
        'notifications': notifications,
        'total_unread_number': total_unread_number,
        "articles_unread_number": articles_unread_number

    }

    return render(request, 'accountapp/personal_area.html', context=context)
