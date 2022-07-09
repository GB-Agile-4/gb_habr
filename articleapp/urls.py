from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import ArticleView, ArticleCreateView, ArticleUpdateView
from . import views

urlpatterns = [
    path('', ArticleView.as_view()),
    path('post/', ArticleCreateView.as_view(), name='post'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('delete/<int:pk>/', views.article_delete, name='delete'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),

]
