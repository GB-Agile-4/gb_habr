from django.core.management.base import BaseCommand
from mainapp.models import ArticleCategory
from article.models import Article

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

import json, os

User = get_user_model()

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ArticleCategory.objects.all().delete()
        for category in categories:
            new_category = ArticleCategory(**category)
            new_category.save()
            articles = load_from_json('articles')
            Article.objects.all().delete()
        for article in articles:
            category_name = article["category"]
            # Получаем категорию по имени
            _category = ArticleCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            article['category'] = _category
            new_article = Article(**article)
            new_article.save()
    # Создаем суперпользователя при помощи менеджера модели
    super_user = User.objects.create_superuser('django',
    'django@gbhabr.local', 'gbhabr')