from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import requires_csrf_token
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
import datetime

from commentapp.forms import CommentCreateForm
from .models import Article
from .models import ArticleCategory
from .forms import ArticleCreateForm
from likeapp.models import Mark


class ArticleCategoryView(ListView):
    model = ArticleCategory
    context_object_name = 'categories'
    queryset = ArticleCategory.objects.all()


class ArticleView(ListView):
    model = Article
    queryset = Article.objects.filter(is_active=True, is_moderated=True).order_by('-created_at')


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
        article.views += 1
        article.save()
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
        ctx['time'] = datetime.datetime.now()
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/'


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


@requires_csrf_token
def upload_image_view(request):
    f = request.FILES['image']
    fs = FileSystemStorage()
    fs.location += '/images/'
    filename = str(f).split('.')[0]
    file = fs.save(filename, f)
    file_url = '/media/images/' + filename


    return JsonResponse({'success': 1, 'file': {'url': file_url}})

@requires_csrf_token
def upload_file_view(request):
    f = request.FILES['file']
    fs = FileSystemStorage()
    fs.location += '/files/'
    filename, ext = str(f).split('.')
    file = fs.save(filename, f)
    file_url = '/media/images/' + filename

    return JsonResponse({'success': 1, 'file': {'url': file_url, 'size': fs.size(filename), 'name': str(f),
                                                'extension': ext}})
