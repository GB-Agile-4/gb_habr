from django.urls import path
from mainapp import views as mainapp


app_name = 'content'

urlpatterns = [
    path('articles/<int:pk>/', mainapp.articles, name='articles'),
    path('hubs/', mainapp.hubs, name='hubs', ),
]
