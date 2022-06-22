# Generated by Django 4.0.4 on 2022-06-22 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articleapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='text')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_moderated', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articleapp.article')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
