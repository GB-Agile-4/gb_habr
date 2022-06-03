from django.db import models
from mainapp.models import ArticleCategory
from authapp.models import HabrUser

# NULLABLE = {'null': True, 'blank': True}


class Article(models.Model):
    objects = None
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(max_length=128, verbose_name='название')
    text = models.TextField(verbose_name='текст')
    author = models.ForeignKey(HabrUser, on_delete=models.CASCADE, verbose_name='автор')
    is_active = models.BooleanField(default=True)
    is_moderated = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} ({self.category.name})'

    def delete(self):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True

        self.save()
