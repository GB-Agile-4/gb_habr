from django.db import models

from articleapp.models import Article
from authapp.models import HabrUser
# from notificationapp.models import Notification


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.ForeignKey(HabrUser, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    likes = models.IntegerField(default=0, verbose_name='like')
    dislikes = models.IntegerField(default=0, verbose_name='dislike')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at', )


    def __str__(self):
        return f'Комментарий {self.comment_author} на статью {self.article}'

    def count(self):
        total_comments = Comment.objects.filter(is_active=True, parent__isnull=True).count()
        return total_comments
