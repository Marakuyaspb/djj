from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
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


# CATEGORIES

def category_accessory (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})
def category_arm (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})
def category_bed (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})
def category_corner (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})
def category_k1r (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})
def category_pouf (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})
def category_str (request):
	products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products})

# dynamic products
def single_product(request, id):
	#return HttpResponse(f'Product {id}')
	try:
		product = Product.objects.get(id = id)
	except:
		raise Http404('Такого дивана пока нет :(')

	return render(request,'product/single_product.html', {'single_product': product})