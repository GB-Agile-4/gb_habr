from django.urls import path
from mainapp import views as mainapp


app_name = 'content'

urlpatterns = [
    path('articles/<int:pk>/', mainapp.articles, name='articles'),
    path('news/', mainapp.news, name='news', ),
    path('hubs/', mainapp.hubs, name='hubs', ),
    path('authors/', mainapp.authors, name='authors', ),
    path('companies/', mainapp.companies, name='companies', ),
]
