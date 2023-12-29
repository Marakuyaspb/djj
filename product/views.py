from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.paginator import Paginator
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Category, Collection, Option, Product, ProductImage, SliderInterior
from cart.forms import CartAddProductForm
from .forms import CustomProductForm

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
		popular = Product.objects.filter(popular=True)
		similar_products = Product.objects.filter(collection=product.collection)
	else:
		# handle error case here
		pass
	cart_product_form = CartAddProductForm()
	return render(request,'product/single_product.html', {'product': product, 'options': options, 'slider_interior':slider_interior, 'popular': popular, 'similar_products': similar_products,  'cart_product_form': cart_product_form})




# SINGLE PRODUCT
# def single_product(request):
# 	if request.method == 'POST':
# 		carousel_items = request.FILES.getlist('carousel_items')
# 		carousel_items_mob = request.FILES.getlist('carousel_items_mob')
# 		interior_items = request.FILES.getlist('carousel_items')
# 		interior_items_mob = request.FILES.getlist('carousel_items_mob')
		
# 		product = Product.objects.get(product_slug=product_slug)
		
# 		for image_file in carousel_items:
# 			product_image = ProductImage.objects.create(product=product)
# 			if isinstance(image_file, InMemoryUploadedFile):
# 				image.image.save(image_file.name, image_file)
# 			else:
# 				image.image = image_file
# 			image.save()
# 		for image_file in carousel_items_mob:
# 			product_image = ProductImage.objects.create(product=product)
# 			if isinstance(image_file, InMemoryUploadedFile):
# 				image.image.save(image_file.name, image_file)
# 			else:
# 				image.image = image_file
# 			image.save()
# 		for image_file in interior_items:
# 			product_image = ProductImage.objects.create(product=product)
# 			if isinstance(image_file, InMemoryUploadedFile):
# 				image.image.save(image_file.name, image_file)
# 			else:
# 				image.image = image_file
# 			image.save()
# 		for image_file in interior_items_mob:
# 			product_image = ProductImage.objects.create(product=product)
# 			if isinstance(image_file, InMemoryUploadedFile):
# 				image.image.save(image_file.name, image_file)
# 			else:
# 				image.image = image_file
# 			image.save()


# 			context = {'single_product': product, 'form': form}


# 	return render(request, 'single_product.html', context)








# def single_product(request, product_slug=None):
# 	if product_slug:
# 		product = get_object_or_404(Product, product_slug=product_slug)	
# 		context = {'single_product': product}
# 	else:
# 		# handle error case here
# 		pass

# 	cart_product_form = CartAddProductForm()

# 	return render(request,'product/single_product.html', context)