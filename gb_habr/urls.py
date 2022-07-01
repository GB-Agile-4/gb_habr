from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from mainapp import views as mainapp


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('mainapp.urls', namespace='mainapp')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('user/', include('accountapp.urls', namespace='user')),
    path('article/', include(('articleapp.urls', 'article'), namespace='article')),
    path('search/', include('searchapp.urls', namespace='search')),
<<<<<<<<< Temporary merge branch 1
    path('like/', include('likeapp.urls', namespace='like')),
=========
    path('moder/', include('moderapp.urls', namespace='moder')),
    path('comment/', include('commentapp.urls', namespace='comment')),
>>>>>>>>> Temporary merge branch 2
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
