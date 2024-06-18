from django.db.models import Q, F, Count, Value
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

from .filters import product_ordering, product_filtering, unique_names
from .models import Product, Category, Collection, Color, Producttype, Option, SliderInterior
from cart.forms import CartAddProductForm
from .forms import FilterForm

# # # # # # # # # # # # # #

def error_404_view(request, exception):
	products = Product.objects.all()
	popular = Product.objects.filter(popular=True)
	return render(request, 'product/404/404.html', {'products': products, 'popular': popular}, status=404)

def error_500(request):
	return render(request, 'product/500.html', status=500)

# # # # # # # # # # # # # #



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



def products(request):
	sort_by = request.GET.get('sort_by', 'asc')
	products_list = Product.objects.all()
	products_list = product_ordering(Product, products_list, sort_by)

	if request.method == 'GET':
		queryset = product_filtering(request, products_list)


		selected_options = {}
		for key, value in request.GET.items():
			if key in [ 'collection_ids', 'color_ids', 'linen_drawer', 'mechanism_type', 'paws_type', 'sleep_place', 'type_ids']:
				selected_options[key] = value

		# Create Q objects for filtering
		q_objects = Q()
		for key, value in selected_options.items():
			q_objects &= Q(**{key: value})

		# Filter products based on selected options
		queryset = products_list.filter(q_objects)	


	unique_values = unique_names(request)

	common_products = queryset


	# ADD PAGINATOR
	paginator = Paginator(queryset, 18)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	context = {
		'products': products,
		'sort_by': sort_by,
		'products_list': products_list,
		'queryset': queryset,		
		**unique_values,
	}

	if not queryset:
		context['no_results'] = True

	return render(request, 'product/category_goods.html', context)