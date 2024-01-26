from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.paginator import Paginator
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Category, Collection, Option, Product, ProductImage, SliderInterior
from cart.forms import CartAddProductForm
#from .forms import CustomProductForm

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
		category = get_object_or_404(Category, category='corner')
		products = Product.objects.filter(category=category)
	elif category_slug == 'k1r':
		category = get_object_or_404(Category, category='k1r')
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
def contact(request):
	return render(request, 'product/contact.html')
def payment(request):
	return render(request, 'product/payment.html')
def showrooms(request):
	return render(request, 'product/showrooms.html')
def categories(request):
	return render(request, 'product/categories_list.html')

#ALL
def products (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})


def error_404_view(request, exception):
	products = Product.objects.all()
	popular = Product.objects.filter(popular=True)
	return render(request, '404/404.html', {'products': products, 'popular': popular}, status=404)

def single_product(request, product_slug=None):
	template_name = 'product/single_product.html'  # Default template name
    
	if product_slug:
		product = get_object_or_404(Product, product_slug=product_slug)
		options = product.options.all()
		slider_interior = product.slider_interior
		popover = product.popover
		popular = Product.objects.filter(popular=True)
		similar_products = Product.objects.filter(collection=product.collection)
		if product.category in ['accessory', 'bed', 'corner', 'str']:
			template_name = 'product/single_product.html'
		elif product.category in ['arm']:
			template_name = 'product/single_product_arm.html'
		elif product.category in ['table', 'accessory']:
			template_name = 'product/single_product_simpler.html'
		elif product.category in ['poufl', 'poufs']:
			template_name = 'product/single_product_pouf.html'
		elif product.category in ['k1r']:
			template_name = 'product/single_product_full.html'
		else:
			# handle error case here
			pass

	else:
		# handle error case here
		pass

	cart_product_form = CartAddProductForm()
	return render(request, template_name, {
		'product': product,
		'options': options,
		'slider_interior': slider_interior,
		'popular': popular,
		'similar_products': similar_products,
		'cart_product_form': cart_product_form
	})