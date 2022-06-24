from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse, reverse_lazy

from commentapp.forms import CommentCreateForm
from .models import Article
from .models import ArticleCategory
from .forms import ArticleCreateForm
from commentapp.models import Comment


class ArticleCategoryView(ListView):
    model = ArticleCategory
    context_object_name = 'categories'
    queryset = ArticleCategory.objects.all()


class ArticleView(ListView):
    model = Article
    queryset = Article.objects.all()


# class ArticleDetailView(DetailView):
#     model = Article
#
#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         return ctx


def article_detail(request, pk):
    template_name = 'articleapp/article_detail.html'
    article = get_object_or_404(Article, pk=pk)
    print(article.body, article.author)
    comments = article.comments.filter(is_active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentCreateForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.comment_author = request.user
            new_comment.save()
    else:
        comment_form = CommentCreateForm()

    return render(request, template_name, {'article': article,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


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
    success_url = '/article/'



class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreateForm
    success_url = '/'

