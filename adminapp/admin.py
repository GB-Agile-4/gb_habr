from django.contrib import admin
from articleapp.models import Article, ArticleCategory
from authapp.models import HabrUser, HabrUserProfile
from commentapp.models import Comment
from notificationapp.models import Notification


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'author', 'body', 'created_at', 'updated_at', 'is_active', 'is_moderated', 'is_archived')
#     list_filter = ('category', 'author', 'created_at', 'updated_at', 'is_active', 'is_moderated')
    list_filter = ('author', 'is_active','is_moderated')
    search_fields = ('title', 'body')
    

class HabrUserAdmin(admin.ModelAdmin):
    list_filter = ('is_staff', 'is_banned')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'comment_author', 'body', 'created_at', 'updated_at', 'is_active', 'is_moderated')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('comment_author', 'body')


admin.site.register(ArticleCategory)
admin.site.register(Article, ArticleAdmin)
admin.site.register(HabrUser, HabrUserAdmin)
admin.site.register(HabrUserProfile)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Notification)
