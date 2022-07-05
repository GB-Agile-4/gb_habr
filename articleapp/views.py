from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import requires_csrf_token
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
import datetime


from .models import Article
from .models import ArticleCategory
from .forms import ArticleCreateForm

from mainapp.views import top_articles, articles_read_now


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

    return render(request, template_name, {'article': article,
                                           'comments': comments,
                                           'articles_read_now': articles_read_now(),
                                           'top_articles': top_articles()
                                           })


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