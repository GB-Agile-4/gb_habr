from django import forms

from .models import Article, ArticleCategory


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'body':
                field.label = False
            if field_name == 'title':
                field.widget.attrs['placeholder'] = 'Заголовок'
                field.widget.attrs['class'] = 'article_editor_title'
                field.label = False
            if field_name == 'category':
                field.label = 'Хабы'

            # field.widget.attrs['class'] = 'form-control articleapp-form'
            # field.help_text = ''
