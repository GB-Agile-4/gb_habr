from django.db import models

from articleapp.models import Article
from authapp.models import HabrUser
from commentapp.models import Comment


class Notification(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='notifications')
    article_author = models.ForeignKey(HabrUser, on_delete=models.CASCADE, related_name='notifications')
    comment_author = models.ForeignKey(HabrUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return f'Новый Комментарий на статью {self.article}'

    def count(self, request):
        unread_notifications = Notification.objects.filter(article_author=request.user).exclude(comment_author=request.user)
        return unread_notifications
