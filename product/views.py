from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Collection, Product

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

#ALL
def all_products (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})

# CATEGORIES
def cat_view (request, category_slug=None):
	category = get_object_or_404(Category, category_slug=category_slug)
	products = Product.objects.filter(category=category)
	return render(request, 'product/category_goods.html', {'products': products})
# COLLECTIONS
# def coll_view (request, collection_slug=None):
# 	category = get_object_or_404(Collection, collection_slug=collection_slug)
# 	products = Product.objects.filter(collection=collection)
# 	return render(request, 'product/category_goods.html', {'products': products})

# SINGLE PRODUCT

def single_product(request, product_slug=None):
	if product_slug:
		product = get_object_or_404(Product, product_slug=product_slug)	
	else:
		# handle error case here
		pass

	return render(request,'product/single_product.html', {'single_product': product})


def popular_goods_carousel(request):
	popular = Product.objects.filter(popular=True)
	return render(request, 'popular_goods.html', {'popular': popular})






# def accessory (request):
# 	category='accessory'
# 	products = Product.objects.filter(category__category=category)
# 	return render(request, 'product/category_goods.html', {'products': products})

# def arm (request):
# 	category='arm'
# 	products = Product.objects.filter(category__category=category)
# 	return render(request, 'product/category_goods.html', {'products': products})

# def bed (request, slug):
# 	category='bed'
# 	products = Product.objects.filter(category__category=category)
# 	return render(request, 'product/category_goods.html', {'products': products})

# def corner (request):
# 	category='corner'
# 	products = Product.objects.filter(category__category=category)
# 	return render(request, 'product/category_goods.html', {'products': products})

# def k1r (request):
# 	category='k1r'
# 	products = Product.objects.filter(category__category=category)
# 	return render(request, 'product/category_goods.html', {'products': products})

# def poufl (request):
# 	category='poufl'
# 	products = Product.objects.filter(category__category=category)
# 	return render(request, 'product/category_goods.html', {'products': products})

# def str (request):
# 	category='str'
# 	products = Product.objects.filter(category__category=category)
# 	return render(request, 'product/category_goods.html', {'products': products})