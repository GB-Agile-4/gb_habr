from django.contrib import admin
from articleapp.models import Article, ArticleCategory
from authapp.models import HabrUser, HabrUserProfile
from commentapp.models import Comment


admin.site.register(ArticleCategory)
admin.site.register(HabrUser)
admin.site.register(HabrUserProfile)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'author', 'body', 'created_at', 'updated_at', 'is_active', 'is_moderated', 'is_archived')
    list_filter = ('category', 'author', 'is_active', 'created_at', 'updated_at', 'is_active', 'is_moderated')
    search_fields = ('title', 'body')


admin.site.register(Article)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'comment_author', 'body', 'created_at', 'updated_at', 'is_active', 'is_moderated')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('comment_author', 'body')


admin.site.register(Comment, CommentAdmin)
