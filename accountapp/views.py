from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from datetime import datetime

from articleapp.models import Article
from authapp.models import HabrUser
from notifications.models import Notification

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


def notifications_list(request):
    notifications = request.user.notifications.unread()
    context = {'notifications': notifications}

    return render(request, 'accountapp/notifications_list.html', context=context)


def notifications_delete(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    notification.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
