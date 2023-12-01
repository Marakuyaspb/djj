from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.contrib.sitemaps.views import sitemap
from product.sitemaps import ProductSitemap

app_name = 'product'

sitemaps = {
	'products' : ProductSitemap,
}

urlpatterns = [
	path('', views.index, name = 'index'),
	path('about/', views.about, name = 'about'),
	path('contact/', views.contact, name = 'contact'),
	path('payment/', views.payment, name = 'payment'),
	path('showrooms/', views.showrooms, name = 'showrooms'),

	# category pages 
	path('accessory/', views.accessory, name = 'accessory'),
	path('arm/', views.arm, name = 'arm'),
	path('bed/', views.bed, name = 'bed'),
	path('corner/', views.corner, name = 'corner'),
	path('k1r/', views.k1r, name = 'k1r'),
	path('poufl/', views.poufl, name = 'poufl'),
	path('str/', views.str, name = 'str'),

	# products dynamic
	path('category/<slug:slug>/', views.single_product, name='single_product'),

	# choices
	# path(r'^chaining/', include('smart_selects.urls')),

	#sitemap
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]