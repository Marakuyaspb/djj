from django.urls import path, include
from django.contrib import admin
from product import views
# from django.conf.urls.static import static
# from django.conf import settings

admin.site.site_header = 'Центр управления начинкой сайта'
admin.site.index_title = 'Админская панель'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("product.urls")),
]
