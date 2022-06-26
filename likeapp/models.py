from django.db import models
from authapp.models import HabrUser
from articleapp.models import Article


class Mark(models.Model):
    CHOICES = (
        ("LIKE", "like"),
        ("DISLIKE", "dislike"),
        (None, "None")
    )

    habruser = models.ForeignKey(HabrUser, on_delete=models.CASCADE, related_name='marks')
    marked_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='marks')
    mark = models.CharField(max_length=7, choices=CHOICES, default=None)
