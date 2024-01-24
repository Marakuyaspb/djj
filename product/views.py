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
def cat_view (request, category_slug=None):
	category = get_object_or_404(Category, category_slug=category_slug)
	products = Product.objects.filter(category=category)
	return render(request, 'product/category_goods.html', {'products': products})

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
	if product_slug:
		product = get_object_or_404(Product, product_slug=product_slug)
		options = product.options.all()
		slider_interior = product.slider_interior
		popover = product.popover
		popular = Product.objects.filter(popular=True)
		similar_products = Product.objects.filter(collection=product.collection)
	else:
		# handle error case here
		pass
	cart_product_form = CartAddProductForm()
	return render(request,'product/single_product.html', {'product': product, 'options': options, 'slider_interior':slider_interior, 'popular': popular, 'similar_products': similar_products,  'cart_product_form': cart_product_form})