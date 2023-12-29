from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import reverse
from django.contrib.sitemaps.views import sitemap
from product.sitemaps import ProductSitemap


app_name = 'product'

sitemaps = {
	'all-products' : ProductSitemap,
}


urlpatterns = [
	path('', views.index, name = 'index'),


# just pages
	path('about/', views.about, name = 'about'),
	path('contact/', views.contact, name = 'contact'),
	path('payment/', views.payment, name = 'payment'),
	path('showrooms/', views.showrooms, name = 'showrooms'),
	path('products/', views.products, name = 'products'),
	path('categories/', views.categories, name = 'categories'),


# products dynamic
	path('products/<slug:product_slug>/', views.single_product, name='single_product'),

# category pages 
	path('categories/<str:category_slug>/', views.cat_view, name='cat_view'),




#sitemap
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)