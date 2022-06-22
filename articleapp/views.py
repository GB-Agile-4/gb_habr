from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Article
from .models import ArticleCategory
from .forms import ArticleCreateForm


class ArticleCategoryView(ListView):
    model = ArticleCategory
    context_object_name = 'categories'
    queryset = ArticleCategory.objects.all()


class ArticleView(ListView):
    model = Article
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category'] = ArticleCategoryView.queryset
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/articleapp/'


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreateForm
    success_url = '/'

