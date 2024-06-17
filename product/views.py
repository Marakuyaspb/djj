from django.db.models import Q, F, Count, Value
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

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


class GetParametres:
	def get_collection(self):
		return Collection.objects.all()
	def get_color(self):
		return Color.objects.all()
	def get_producttype(self):
		return Producttype.objects.all()
	def get_mechanism_type(self):
		mechanism_types = Product.objects.values_list('mechanism_type', flat=True)
		unique_mechanism_types = set(mechanism_types)
		return unique_mechanism_types
	def get_paws_type(self):
		paws_types = Product.objects.values_list('paws_type', flat=True)
		unique_paws_types = set(paws_types)
		return unique_paws_types



def products(request):
	# SORT BY PRICE
	sort_by = request.GET.get('sort_by', 'asc')
	
	if sort_by == 'asc':
		products_list = Product.objects.all().order_by('price')
	elif sort_by == 'desc':
		products_list = Product.objects.all().order_by('-price')
	else:
		products_list = Product.objects.all()


	if request.method == 'GET':
		filters = Q()

		min_price = (request.GET.get('min_price'))
		max_price = request.GET.get('max_price')
		min_width = request.GET.get('min_width')
		max_width = request.GET.get('max_width')
		min_depth = request.GET.get('min_depth')
		max_depth = request.GET.get('max_depth')
		collection = request.GET.get('collection')
		color_id = request.GET.get('color_id')
		type_id = request.GET.get('type_id')
		paws_type = request.GET.get('paws_type')
		mechanism_type = request.GET.get('mechanism_type')
		linen_drawer = request.GET.get('linen_drawer')

		if min_price:
			filters |= Q(price__gte=min_price)
		if max_price:
			filters |= Q(price__lte=max_price)
		if min_width:
			filters |= Q(width__gte=min_width)
		if max_width:
			filters |= Q(width__lte=max_width)
		if min_depth:
			filters |= Q(depth__gte=min_depth)
		if max_depth:
			filters |= Q(depth__lte=max_depth)
		if collection:
			filters |= Q(collection_name__in=collection)
		if color_id:
			filters |= Q(color_id=color_id)
		if type_id:
			filters |= Q(type_id=type_id)
		if paws_type:
			filters |= Q(paws_type=paws_type)
		if mechanism_type:
			filters |= Q(mechanism_type=mechanism_type)
		if linen_drawer:
			filters |= Q(linen_drawer=linen_drawer)

		queryset = Product.objects.filter(filters)

	unique_product_type = Producttype.objects.values('type_ru').distinct()
	unique_color = Color.objects.values('color_name', 'color_id', 'color_code').distinct()
	unique_collection = Collection.objects.values('collection').annotate(total=Count('collection')).distinct()
	unique_paws_type = Product.objects.values('paws_type').annotate(total=Count('paws_type')).order_by('paws_type').distinct()
	unique_mechanism_type = Product.objects.values('mechanism_type').annotate(total=Count('mechanism_type')).order_by('mechanism_type').distinct()

	# ADD PAGINATOR
	paginator = Paginator(products_list, 18)
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
		'unique_product_type': unique_product_type,
		'unique_color': unique_color,
		'unique_mechanism_type': unique_mechanism_type,
		'unique_paws_type': unique_paws_type,
		'unique_collection': unique_collection,
	}

	if not queryset:
		context['no_results'] = True

	return render(request, 'product/category_goods.html', context)





# def products(request):
# 	# SORT BY PRICE

# 	sort_by = request.GET.get('sort_by', 'asc')
# 	if sort_by == 'asc':
# 		queryset = Product.objects.all().order_by('price')
# 	elif sort_by == 'desc':
# 		queryset = Product.objects.all().order_by('-price')
# 	else:
# 		queryset = Product.objects.all()
# 	queryset = Product.objects.all()





# 	paginator = Paginator(queryset, 9)
# 	page = request.GET.get('page')
# 	try:
# 		products = paginator.page(page)
# 	except PageNotAnInteger:
# 		products = paginator.page(1)
# 	except EmptyPage:
# 		products = paginator.page(paginator.num_pages)

# 	context = {
# 		'sort_by': sort_by,
# 		'products': products,

# 	}

# 	return render(request, 'product/category_goods.html', context)



# def products(request):
# 	# SORT BY PRICE
# 	sort_by = request.GET.get('sort_by', 'asc')
# 	if sort_by == 'asc':
# 		products_list = Product.objects.all().order_by('price')
# 	elif sort_by == 'desc':
# 		products_list = Product.objects.all().order_by('-price')
# 	else:
# 		products_list = Product.objects.all()

# 	if request.method == 'POST':
# 		filter_form = FilterForm(request.POST)
# 		if filter_form.is_valid():
# 			min_price = filter_form.cleaned_data.get('min_price')
# 			max_price = filter_form.cleaned_data.get('max_price')
# 			min_width = filter_form.cleaned_data.get('min_width')
# 			max_width = filter_form.cleaned_data.get('max_width')
# 			min_depth = filter_form.cleaned_data.get('min_depth')
# 			max_depth = filter_form.cleaned_data.get('max_depth')

# 			queryset = Product.objects.filter(
# 				Q(collection__in=filter_form.cleaned_data.get('collections')) |
# 				Q(fabric_name__product_fabric_color__color_name__in=filter_form.cleaned_data.get('colors')) |
# 				Q(category__type_ru__in=filter_form.cleaned_data.get('producttypes')) |
# 				Q(price__gte=min_price) |
# 				Q(price__lte=max_price) |
# 				Q(width__gte=min_width) |
# 				Q(width__lte=max_width) |
# 				Q(depth__gte=min_depth) |
# 				Q(depth__lte=max_depth)
# 			)
# 			products_list = queryset

# 	unique_product_type = Producttype.objects.values('type_ru').distinct()
# 	unique_color = Color.objects.values('color_name', 'color_id', 'color_code').distinct()
# 	unique_collection = Collection.objects.values('collection').annotate(total=Count('collection')).distinct()
# 	unique_paws_type = Product.objects.values('paws_type').annotate(total=Count('paws_type')).distinct()
# 	unique_mechanism_type = Product.objects.values('mechanism_type').distinct()

# 	print(unique_color)
# 	# ADD PAGINATOR
# 	paginator = Paginator(products_list, 9)
# 	page = request.GET.get('page')
# 	try:
# 		products = paginator.page(page)
# 	except PageNotAnInteger:
# 		products = paginator.page(1)
# 	except EmptyPage:
# 		products = paginator.page(paginator.num_pages)

# 	context = {
# 		'products': products,
# 		'products_list': products_list,
# 		'sort_by': sort_by,
# 		'filter_form': FilterForm(),
# 		'unique_product_type': unique_product_type,
# 		'unique_color': unique_color,
# 		'unique_mechanism_type': unique_mechanism_type,
# 		'unique_paws_type': unique_paws_type,
# 		'unique_collection': unique_collection,
# 	}
	
# 	return render(request, 'product/category_goods.html', context)





# class FilterProductsView(GetParametres, View):
# 	def get_queryset(self, request):
# 		queryset = Product.objects.filter(
# 			Q(collection__in=self.request.GET.getlist('collection')) |
# 			Q(color__in=self.request.GET.getlist('color')) |
# 			Q(producttype__in=self.request.GET.getlist('producttype')) |
# 			Q(unique_mechanism_types__in=self.request.GET.getlist('unique_mechanism_types')) |
# 			Q(unique_paws_types__in=self.request.GET.getlist('unique_paws_types')) |
# 			Q(price__gte=min_price) |
# 			Q(price__lte=max_price) |
# 			Q(width__gte=min_width) |
# 			Q(width__lte=max_width) |
# 			Q(depth__gte=min_depth) |
# 			Q(depth__lte=max_depth)
#         )
# 		context = {
# 			'products': queryset
# 		}
# 		return render(request, 'product/category_goods.html', context)

# filter_products_view = FilterProductsView.as_view()



#ALL FILTER 
# def products (request):
# 	products = Product.objects.all()
	
# 	view = GetParametres()
# 	collections = view.get_collection()
# 	colors = view.get_color()
# 	producttypes = view.get_producttype()
	

# 	if request.method == 'GET':
# 		form = FilterForm(request.GET)
# 		if form.is_valid():
# 			min_price = form.cleaned_data.get('min_price')
# 			max_price = form.cleaned_data.get('max_price')
# 			collections = form.cleaned_data.get('collections')
# 			colors = form.cleaned_data.get('colors')

# 			if min_price is None:
# 				min_price = 0
# 			if max_price is None:
# 				max_price = 400000
 
# 			if min_price is not None:
# 				products = products.filter(price__gte=min_price)
# 			if max_price is not None:
# 				products = products.filter(price__lte=max_price)

# 			products = Product.objects.filter(price__gte=min_price, price__lte=max_price)

# 			if collections:
# 				products = products.filter(collection__in=collections)

# 			if colors:
# 				products = products.filter(fabric_name__product_fabric_color__in=colors)

# 	else:
# 		form = FilterForm()



# 	context = {
# 		'products': products,
# 		'form': form,
# 		'view': view,
# 		'categories': categories,
# 		'collections': collections,
# 		'colors': colors,
# 		'producttypes': producttypes
# 		}


# 	return render(request, 'product/category_goods.html', context)