from django.urls import path, include
from django.contrib import admin
from product import views
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Сверхважный Центр Управления Контентом'
admin.site.index_title = 'Админская панель'

handler404 = views.error_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("cart/", include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('product/', include('product.urls', namespace='payment')),
    path("", include("blog.urls")),
    path("", include("product.urls")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)