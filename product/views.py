from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.paginator import Paginator
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Category, Collection, Option, Product, ProductImage, SliderInterior
from cart.forms import CartAddProductForm


def index(request):
	products = Product.objects.all()
	popular = Product.objects.filter(popular=True)
	return render(request, 'product/index.html', {'products': products, 'popular': popular})

# CATEGORIES
def cat_view(request, category_slug=None):
	if category_slug == 'poufl':
		poufl_category = get_object_or_404(Category, category='poufl')
		poufs_category = get_object_or_404(Category, category='poufs')
		products = Product.objects.filter(category__in=[poufl_category, poufs_category])
	elif category_slug == 'accessory':
		category = get_object_or_404(Category, category='accessory')
		products = Product.objects.filter(category=category)
	elif category_slug == 'arm':
		category = get_object_or_404(Category, category='arm')
		products = Product.objects.filter(category=category)
	elif category_slug == 'bed':
		category = get_object_or_404(Category, category='bed')
		products = Product.objects.filter(category=category)
	elif category_slug == 'corner':
		category = get_object_or_404(Category, category='cornerl')
		products = Product.objects.filter(category=category)
	elif category_slug == 'mod':
		category = get_object_or_404(Category, category='mod1')
		products = Product.objects.filter(category=category)
	elif category_slug == 'str':
		category = get_object_or_404(Category, category='str')
		products = Product.objects.filter(category=category)
	elif category_slug == 'table':
		category = get_object_or_404(Category, category='table')
		products = Product.objects.filter(category=category)
	else:
		products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})

# def cat_view (request, category_slug=None):
# 	category = get_object_or_404(Category, category_slug=category_slug)
# 	products = Product.objects.filter(category=category)
# 	return render(request, 'product/category_goods.html', {'products': products})


def about(request):
	return render(request, 'product/about.html')
def categories(request):
	return render(request, 'product/categories_list.html')
def contact(request):
	return render(request, 'product/contact.html')
def dealers(request):
	return render(request, 'product/dealers.html')
def designers(request):
	return render(request, 'product/designers.html')
def payment(request):
	return render(request, 'product/payment.html')
def showrooms(request):
	return render(request, 'product/showrooms.html')
def vacancies(request):
	return render(request, 'product/vacancies.html')



#ALL
def products (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})


def error_404_view(request, exception):
	products = Product.objects.all()
	popular = Product.objects.filter(popular=True)
	return render(request, '404/404.html', {'products': products, 'popular': popular}, status=404)

def single_product(request, product_slug=None):
	cart_product_form = CartAddProductForm()
    
	if product_slug:
		product = get_object_or_404(Product, product_slug=product_slug)
		options = product.options.all()
		slider_interior = product.slider_interior
		popover = product.popover
		popular = Product.objects.filter(popular=True)
		similar_products = Product.objects.filter(collection=product.collection)

		return render(request, 'product/single_product.html', {
			'product': product,
			'options': options,
			'slider_interior': slider_interior,
			'popular': popular,
			'similar_products': similar_products,
			'cart_product_form': cart_product_form
			})