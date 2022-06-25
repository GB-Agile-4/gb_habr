from django.urls import path

from .views import ArticleView, ArticleCreateView, ArticleDeleteView, ArticleUpdateView
from . import views

urlpatterns = [
    path('', ArticleView.as_view()),
    path('post/', ArticleCreateView.as_view(), name='post'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),

]
