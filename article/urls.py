from django.urls import path

from .views import ArticleView, ArticleCreateView, ArticleDetailView, ArticleDeleteView, ArticleUpdateView


urlpatterns = [
    path('', ArticleView.as_view()),
    path('post/', ArticleCreateView.as_view(), name='post'),
    path('<int:pk>/', ArticleDetailView.as_view()),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),

]
