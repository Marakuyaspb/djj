from django.urls import path
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
	path('category_accessory/', views.showrooms, name = 'category_accessory'),
	path('category_arm/', views.category_arm, name = 'category_arm'),
	path('category_bed/', views.showrooms, name = 'category_bed'),
	path('category_corner/', views.showrooms, name = 'category_corner'),
	path('category_k1r/', views.showrooms, name = 'category_k1r'),
	path('category_poufl/', views.showrooms, name = 'category_poufl'),
	path('category_poufs/', views.showrooms, name = 'category_poufs'),
	path('category_str/', views.showrooms, name = 'category_str'),

	# products dynamic
	path('category_arm/<int:id>/', views.single_product, name='single_product'),

	#sitemap
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]