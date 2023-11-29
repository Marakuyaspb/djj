from django.urls import path, include
from django.contrib import admin
from product import views
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Центр управления начинкой сайта'
admin.site.index_title = 'Админская панель'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("product.urls")),
    path("", include("blog.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)