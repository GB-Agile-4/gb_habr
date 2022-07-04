from django.urls import path
from mainapp import views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('articles/<int:pk>/', mainapp.articles, name='articles'),
    path('help/', mainapp.help, name='help', ),
]
