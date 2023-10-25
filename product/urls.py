from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('about/', views.about, name = 'about'),
	path('category_goods/', views.category_goods, name = 'category_goods'),
	path('contact/', views.contact, name = 'contact'),
	path('payment/', views.payment, name = 'payment'),
	path('showrooms/', views.showrooms, name = 'showrooms'),
]