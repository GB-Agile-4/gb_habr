from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect

from commentapp.forms import CommentCreateForm
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


def article_detail(request, pk):
    template_name = 'articleapp/article_detail.html'
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.filter(is_active=True).order_by('-created_at')
    new_comment = None

    if request.method == 'POST':
        if request.user.is_banned:
            return HttpResponseRedirect(reverse('accountapp:account', args=[request.user.username]))
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

    def get(self, request, *args, **kwargs):
        if request.user.is_banned:
            return HttpResponseRedirect(reverse('accountapp:account', args=[request.user.username]))
        return super().get(request, *args, **kwargs)

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

    def get(self, request, *args, **kwargs):
        if request.user.is_banned:
            return HttpResponseRedirect(reverse('accountapp:account', args=[request.user.username]))
        return super().get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_moderated = False
        self.object.save()
        return super().post(request, *args, **kwargs)
