from django.db import models
from authapp.models import HabrUser
from articleapp.models import Article
from commentapp.models import Comment


class Mark(models.Model):
    CHOICES = (
        ("LIKE", "like"),
        ("DISLIKE", "dislike")
    )

    habruser = models.ForeignKey(HabrUser, on_delete=models.CASCADE, related_name='marks')
    marked_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='marks')
    mark = models.CharField(max_length=7, choices=CHOICES, default=None)


class CommentMark(models.Model):
    CHOICES = (
        ("LIKE", "like"),
        ("DISLIKE", "dislike")
    )

    habruser = models.ForeignKey(HabrUser, on_delete=models.CASCADE, related_name='comment_marks')
    marked_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_marks')
    mark = models.CharField(max_length=7, choices=CHOICES, default=None)
