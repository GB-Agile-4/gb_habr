from django.shortcuts import render

from articleapp.models import Article


def search(request):
    sort_order = {'title': 'По названию',
                  'created_at': 'Сначала свежие',
                  'rating': 'Сначала с высоким рейтингом'}

    if request.method == 'POST':
        title = request.POST.get('title')

    else:
        title = request.GET.get('title')

    if title:
        order = request.GET.get('order', 'title')
        articles = Article.objects.filter(title__icontains=title).order_by(f'-{order}')
        context = {'articles': articles, 'query': title, 'order': sort_order.get(order)}
        return render(request, 'searchapp/search.html', context=context)

    return render(request, 'searchapp/search.html')
