from django.shortcuts import render

from article.models import Article


def search(request):
    if request.method == 'POST':
        title = request.POST.get('to_search')
        articles = Article.objects.filter(title=title)

        context = {'articles': articles}

        return render(request, 'searchapp/search.html', context=context)

    return render(request, 'searchapp/search.html')
