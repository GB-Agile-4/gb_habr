from django.contrib import admin
from article.models import Article
from mainapp.models import ArticleCategory
from authapp.models import HabrUser, HabrUserProfile


admin.site.register(ArticleCategory)
admin.site.register(Article)
admin.site.register(HabrUser)
admin.site.register(HabrUserProfile)
