from django.shortcuts import render, get_object_or_404, redirect

from .models import Mark
from articleapp.models import Article


def add_like(request, pk):
    template_name = 'articleapp/article_detail.html'
    article = get_object_or_404(Article, pk=pk)

    if request.user.is_authenticated:
        if Mark.objects.filter(habruser=request.user, marked_article=article):
            user_mark = Mark.objects.get(habruser=request.user, marked_article=article)
            if user_mark.mark == 'like':
                user_mark.delete()
                article.likes -= 1
                article.save()

            elif user_mark.mark == 'dislike':
                user_mark.delete()
                user_mark = Mark(habruser=request.user, marked_article=article, mark='like')
                article.likes += 1
                article.dislikes -= 1
                article.save()
                user_mark.save()

        else:
            if request.user != article.author:
                user_mark = Mark(habruser=request.user, marked_article=article, mark='like')
                article.likes += 1
                article.save()
                user_mark.save()

    comments = article.comments.filter(is_active=True).order_by('-created_at')

    return redirect(request.GET.get('next', '/'))
    # return render(request, template_name, {'article': article,'comments': comments})


def add_dislike(request, pk):
    template_name = 'articleapp/article_detail.html'
    article = get_object_or_404(Article, pk=pk)

    if request.user.is_authenticated:
        if Mark.objects.filter(habruser=request.user, marked_article=article):
            user_mark = Mark.objects.get(habruser=request.user, marked_article=article)
            if user_mark.mark == 'dislike':
                user_mark.delete()
                article.dislikes -= 1
                article.save()

            elif user_mark.mark == 'like':
                user_mark.delete()
                user_mark = Mark(habruser=request.user, marked_article=article, mark='dislike')
                article.dislikes += 1
                article.likes -= 1
                article.save()
                user_mark.save()

        else:
            if request.user != article.author:
                user_mark = Mark(habruser=request.user, marked_article=article, mark='dislike')
                article.dislikes += 1
                article.save()
                user_mark.save()

    comments = article.comments.filter(is_active=True).order_by('-created_at')

    return redirect(request.GET.get('next', '/'))
    # return render(request, template_name, {'article': article,
    #                                        'comments': comments})
