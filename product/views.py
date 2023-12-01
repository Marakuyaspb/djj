from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category
from .models import Product

def index(request):
	return render(request, 'product/index.html')
def about(request):
	return render(request, 'product/about.html')
def contact(request):
	return render(request, 'product/contact.html')
def payment(request):
	return render(request, 'product/payment.html')
def showrooms(request):
	return render(request, 'product/showrooms.html')



# dynamic products

def single_product(request, id=None, slug=None):
	if id:
		product = get_object_or_404(Product, id=id)
	elif slug:
		product = get_object_or_404(Product, slug=slug)
	else:
		# handle error case here
		pass

	return render(request,'product/single_product.html', {'single_product': product})


def popular_goods_carousel(request):
	popular = Product.objects.filter(popular=True)
	return render(request, 'popular_goods.html', {'popular': popular})

# CATEGORIES


def accessory (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})


def arm (request):
	products = Product.objects.filter(category='arm')
	# collection, category, fabric_name = slug.split('-')
	category_obj = Category.objects.get(collection=collection, category=category, fabric_name=fabric_name)
	context = {
        'category': category_obj,
    }
	return render(request, 'product/category_goods.html', {'products': products}, context)


def bed (request, slug):
	products = Product.objects.filter(category='bed')
	collection, category, fabric_name = slug.split('-')
	category_obj = Category.objects.get(collection=collection, category=category, fabric_name=fabric_name)
	context = {
        'category': category_obj,
    }
	return render(request, 'product/category_goods.html', {'products': products}, context)


def corner (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})
def k1r (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})
def poufl (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})
def str (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})

# def category_page(request, slug):
#     category = Category.objects.get(slug=slug)
#     products = Product.objects.filter(category=category)
#     return render(request, 'product/category_goods.html', {'products': products})