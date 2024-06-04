from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.paginator import Paginator
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Category, Collection, Color, Producttype, Option, Product, SliderInterior
from cart.forms import CartAddProductForm


# # # # # # # # # # # # # #

def error_404_view(request, exception):
	products = Product.objects.all()
	popular = Product.objects.filter(popular=True)
	return render(request, '404/404.html', {'products': products, 'popular': popular}, status=404)

def error_500(request):
	return render(request, 'product/500.html', status=500)

# # # # # # # # # # # # # #


class GetParametres:

	def get_category(self):
		return Category.objects.all()

	def get_collection(self):
		return Collection.objects.all()

	def get_color(self):
		return Color.objects.all()

	def get_producttype(self):
		return Producttype.objects.all()




def filter_products(request):
	collections = request.GET.getlist('collection')
	colors = request.GET.getlist('color')

	products = Product.objects.all()

	if collections:
		products = products.filter(collection__in=collections)

	if colors:
		products = products.filter(fabric_name__product_fabric_color__in=colors)

	return render(request, 'category_goods.html', {'products': products})




def index(request):
	products = Product.objects.all()
	popular = Product.objects.filter(popular=True)
	return render(request, 'product/index.html', {'products': products, 'popular': popular})

# CATEGORIES
def category_list(request):
	categories = Category.objects.all()
	return render(request, 'category_list.html', {'categories': categories, 'products': products, 'popular': popular})


def cat_view(request, category_slug=None):
	view = GetParametres()
	categories = view.get_category()
	collections = view.get_collection()
	colors = view.get_color()
	producttypes = view.get_producttype()
	
	if category_slug == 'poufl':
		poufl_category = get_object_or_404(Category, category='poufl')
		poufs_category = get_object_or_404(Category, category='poufs')
		products = Product.objects.filter(category__in=[poufl_category, poufs_category])
	elif category_slug == 'poufs':
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
		cornerl_category = get_object_or_404(Category, category='cornerl')
		corner_r_category = get_object_or_404(Category, category='corner_r')
		products = Product.objects.filter(category__in=[cornerl_category, corner_r_category])
	elif category_slug == 'mod1':
		mod1_category = get_object_or_404(Category, category='mod1')
		products = Product.objects.filter(category=mod1_category)
	elif category_slug == 'str':
		sofa_2m_st_category = get_object_or_404(Category, category='sofa_2m_st')
		sofa_2m_n_category = get_object_or_404(Category, category='sofa_2m_st')
		sofa_3m_st_category = get_object_or_404(Category, category='sofa_3m_st')
		sofa_3m_n_category = get_object_or_404(Category, category='sofa_3m_n')
		sofa_maxi_st_category = get_object_or_404(Category, category='sofa_maxi_st')
		sofa_maxi_n_category = get_object_or_404(Category, category='sofa_maxi_n')
		products = Product.objects.filter(category__in=[sofa_2m_st_category, sofa_2m_n_category, sofa_3m_st_category, sofa_3m_n_category, sofa_maxi_st_category, sofa_maxi_n_category])
	elif category_slug == 'table':
		category = get_object_or_404(Category, category='table')
		products = Product.objects.filter(category=category)
	else:
		products = Product.objects.all()
	return render(request, 'product/category_goods.html', {'products': products, 'view': view, 'categories': categories, 'collections': collections, 'colors': colors, 'producttypes': producttypes})



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
def privacy(request):
	return render(request, 'product/privacy-policy.html')
def showrooms(request):
	return render(request, 'product/showrooms.html')
def vacancies(request):
	return render(request, 'product/vacancies.html')



#ALL FILTER 
def products (request):
	view = GetParametres()
	categories = view.get_category()
	collections = view.get_collection()
	colors = view.get_color()
	producttypes = view.get_producttype()
	products = Product.objects.all()

	return render(request, 'product/category_goods.html', {
		'products': products,
		'view': view,
		'categories': categories,
		'collections': collections,
		'colors': colors,
		'producttypes': producttypes
	})








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