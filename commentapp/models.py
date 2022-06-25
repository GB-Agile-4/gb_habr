from django.db import models
from articleapp.models import Article
from authapp.models import HabrUser



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.ForeignKey(HabrUser, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created_at', )


    def __str__(self):
        return f'Комментарий {self.comment_author} на статью {self.article}'