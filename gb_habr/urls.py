from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from mainapp import views as mainapp
from articleapp import views as articleapp


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('mainapp.urls', namespace='mainapp')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('user/', include('accountapp.urls', namespace='user')),
    path('article/', include(('articleapp.urls', 'article'), namespace='article')),
    path('search/', include('searchapp.urls', namespace='search')),
    path('uploadi/', csrf_exempt(articleapp.upload_image_view)),
    path('uploadf/', csrf_exempt(articleapp.upload_file_view)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
