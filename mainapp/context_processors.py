from articleapp.models import ArticleCategory


def article_categories(request):
    article_categories = ArticleCategory.objects.all()

    return {'article_categories': article_categories}
