from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Collection, Product, ProductImage
# from .forms import ProductForm, ProductImageForm


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


# SINGLE PRODUCT

def single_product(request, product_slug=None):
	if product_slug:
		product = get_object_or_404(Product, product_slug=product_slug)	
		context = {'single_product': product}
	else:
		# handle error case here
		pass

	return render(request,'product/single_product.html', context)



# def single_product(request):
# 	if request.method == 'POST':
# 		product_form = ProductForm(request.POST)
# 		image_form = ProductImageForm(request.POST, request.FILES)
# 		if product_form.is_valid() and image_form.is_valid():
# 			product = product_form.save()
# 			for image in request.FILES.getlist('images'):
# 				product_image = ProductImage.objects.create(image=image)
# 				product_image.product = product
# 				product_image.save()
# 			return redirect('single_product', product_slug=product.product_slug)
# 	else:
# 		product_form = ProductForm()
# 		image_form = ProductImageForm()
# 	return render(request, 'single_product.html', {'product_form': product_form, 'image_form': image_form})




def popular_goods_carousel(request):
	popular = Product.objects.filter(popular=True)
	return render(request, 'popular_goods.html', {'popular': popular})

# COLLECTIONS
def coll_view (request, collection_slug=None):
	collection = get_object_or_404(Collection, collection_slug=collection_slug)
	products = Product.objects.filter(collection=collection)
	return render(request, 'product/category_goods.html', {'products': products})