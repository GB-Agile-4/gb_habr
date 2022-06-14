from django.contrib import admin
from article.models import Article
from authapp.models import HabrUser, HabrUserProfile
from mainapp.models import ArticleCategory


admin.site.register(Article)
admin.site.register(ArticleCategory)
admin.site.register(HabrUser)
admin.site.register(HabrUserProfile)
