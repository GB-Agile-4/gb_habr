from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler as BS
from notifications.signals import notify

from articleapp.models import Article
from authapp.models import HabrUser


def start_scheduler():
    scheduler = BS()
    scheduler.add_job(check_scheduled_unbans, "interval", minutes=10, id="unban_manager", replace_existing=True)
    scheduler.start()


def check_scheduled_unbans():
    print("Checking expired bans...")
    today = datetime.now().date()
    banned_users = HabrUser.objects.filter(is_banned=True)
    for user in banned_users:
        if user.banned_till <= today:
            user.is_banned = False
            user.save()


def ban_user(request, pk):

    habr_user = HabrUser.objects.filter(pk=pk).first()

    if habr_user.is_banned:
        habr_user.is_banned = False
    else:
        time_now = datetime.now().date()
        habr_user.is_banned = True
        habr_user.banned_till = time_now + timedelta(days=14)
        print(habr_user.banned_till)

        notify.send(request.user, recipient=habr_user, action_object=habr_user, description='habr_user',
                    verb=f'Вы нарушили правила сайта и теперь вы не можете писать статьи, \
                     оставлять комментарии и ставить лайки в течение следующих 2 недель.')

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

    notify.send(request.user, recipient=article.author, action_object=article, description='article',
                verb=f'Ваша статья {article.title} успешно прошла модерацию.')

    return HttpResponseRedirect(reverse('moderapp:moderate_list'))


def reject_moderate_post(request, pk):
    article = Article.objects.filter(pk=pk).first()

    article.reject_moderation = True
    article.save()

    return HttpResponseRedirect(reverse('moderapp:moderate_list'))