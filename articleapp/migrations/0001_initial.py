# Generated by Django 4.0.5 on 2022-07-03 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_editorjs.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'Categories',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='название')),
                ('body', django_editorjs.fields.EditorJsField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_moderated', models.BooleanField(default=False)),
                ('reject_moderation', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0, verbose_name='like')),
                ('dislikes', models.IntegerField(default=0, verbose_name='dislike')),
                ('rating', models.IntegerField(default=0, verbose_name='рейтинг')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='просмотры')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articleapp.articlecategory', verbose_name='категория')),
            ],
        ),
    ]
