Product.objects.values("price", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")

Product.objects.values("", "", "", "cat__name")



# data which displays on category_goods.html page
"product_slug",
"is_new",
"available_in_showroom",
"available_for_delivery_2",
"product_img",
"product_img_mob",
"price_old",
"color_code",
"color_id",

"collection",
"fabric_name__product_fabric_color__color_name",
"category_type_ru",
"price",
"width",
"depth",
"height",
"mechanism_type",
"paws_type",
"sleep_place",
"linen_drawer"



name='type_id'
name='collection'
name="color_id"
name='paws_type'
name='mechanism_type'
name='sleep_place'
name='linen_drawer'


class Product(models.Model):
	collection = models.ForeignKey(Collection,
		on_delete=models.CASCADE)
	fabric_name = models.ForeignKey(Fabric,on_delete=models.CASCADE)
	price = models.IntegerField(blank=True,null=True)
	width = models.IntegerField(blank=True, null=True)
	depth = models.IntegerField(blank=True, null=True)
	paws_type = models.CharField(max_length=50, null=True, blank=True)
	mechanism_type = models.CharField(max_length=50, null=True, blank=True)
	linen_drawer = models.CharField(max_length=50, null=True, blank=True)

	@property
	def fabric_color(self):
		return self.fabric_name.product_fabric_color
	@property
	def type_id(self):
		return self.category.type_id




	# if sort_by == 'asc':
	# 	products_list = Product.objects.all().order_by('price')
	# elif sort_by == 'desc':
	# 	products_list = Product.objects.all().order_by('-price')
	# else:
	# 	products_list = Product.objects.all()
	
if request.method == 'POST':
		queryset = Product.objects.filter(
			Q(collection__in=self.request.GET.getlist('collection')) |
			Q(fabric_name__product_fabric_color__color_name__in=self.request.GET.getlist('color')) |
			Q(producttype__in=self.request.GET.getlist('producttype')) |
			Q(unique_mechanism_types__in=self.request.GET.getlist('unique_mechanism_types')) |
			Q(unique_paws_types__in=self.request.GET.getlist('unique_paws_types')) |
			Q(price__gte=min_price) |
			Q(price__lte=max_price) |
			Q(width__gte=min_width) |
			Q(width__lte=max_width) |
			Q(depth__gte=min_depth) |
			Q(depth__lte=max_depth)
        )
		products_set = queryset
	else:
		paginator = Paginator(products_list, 9)
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
		'collections': GetParametres().get_collection(),
		'colors': GetParametres().get_color(),
		'producttypes': GetParametres().get_producttype(),
		'mechanism_types': GetParametres().get_mechanism_type(),
		'paws_types': GetParametres().get_paws_type()

	}

	return render(request, 'product/category_goods.html', context)




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



################################################
################################################



def products(request):

	products = Product.objects.values_list(
		"product_slug",
		"is_new",
		"available_in_showroom",
		"available_for_delivery_2",
		"product_img",
		"product_img_mob",
		"price_old",
		"fabric_name__product_fabric_color__color_code",
		"fabric_name__product_fabric_color__color_id",
		"collection",
		"fabric_name__product_fabric_color__color_name",
		"category__type_ru",
		"price",
		"width",
		"depth",
		"height",
		"mechanism_type",
		"paws_type",
		"sleep_place",
		"linen_drawer")
	sort_by = request.GET.get('sort_by', 'asc')
	if sort_by == 'asc':
		products_list = products.order_by('price')
	elif sort_by == 'desc':
		products_list = products.order_by('-price')
	else:
		products_list = products.all()
	#print(f'My products_list: {products_list}')

	paginator = Paginator(products_list, 9)
	page = request.GET.get('page')

	try:
		products_paginated = paginator.page(page)
	except PageNotAnInteger:
		products_paginated = paginator.page(1)
	except EmptyPage:
		products_paginated = paginator.page(paginator.num_pages)
	# print(f'My products_paginated are: {products_paginated}')
	
	context = {
		'products': products,
		'sort_by': sort_by
	}
	print(f'My products are: {products}')
	return render(request, 'product/category_goods.html', context)

#################################################################





def products(request):
	sort_by = request.GET.get('sort_by', 'asc')
	if sort_by == 'asc':
		products_list = Product.objects.all().order_by('price')
	elif sort_by == 'desc':
		products_list = Product.objects.all().order_by('-price')
	else:
		products_list = Product.objects.all()
	

	if request.method == 'POST':
		queryset = Product.objects.filter(
			Q(collection__in=self.request.GET.getlist('collection')) |
			Q(fabric_name__product_fabric_color__color_name__in=self.request.GET.getlist('color')) |
			Q(producttype__in=self.request.GET.getlist('producttype')) |
			Q(unique_mechanism_types__in=self.request.GET.getlist('unique_mechanism_types')) |
			Q(unique_paws_types__in=self.request.GET.getlist('unique_paws_types')) |
			Q(price__gte=min_price) |
			Q(price__lte=max_price) |
			Q(width__gte=min_width) |
			Q(width__lte=max_width) |
			Q(depth__gte=min_depth) |
			Q(depth__lte=max_depth)
        )
		products = queryset
	else:
		paginator = Paginator(products_list, 9)
		page = request.GET.get('page')

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	context = {
		'products': products,
		'products_list': products_list,
		'sort_by': sort_by,
		'collections': GetParametres().get_collection(),
		'colors': GetParametres().get_color(),
		'producttypes': GetParametres().get_producttype(),
		'mechanism_types': GetParametres().get_mechanism_type(),
		'paws_types': GetParametres().get_paws_type()
	}

	return render(request, 'product/category_goods.html', context)

	#####################################
	#####################################
	#####################################



	def products(request):
	# SORT BY PRICE
	sort_by = request.GET.get('sort_by', 'asc')
	
	if sort_by == 'asc':
		products_list = Product.objects.all().order_by('price')
	elif sort_by == 'desc':
		products_list = Product.objects.all().order_by('-price')
	else:
		products_list = Product.objects.all()

	if request.method == 'POST':
		filter_form = FilterForm(request.POST)
		if filter_form.is_valid():
			min_price = filter_form.cleaned_data.get('min_price')
			max_price = filter_form.cleaned_data.get('max_price')
			min_width = filter_form.cleaned_data.get('min_width')
			max_width = filter_form.cleaned_data.get('max_width')
			min_depth = filter_form.cleaned_data.get('min_depth')
			max_depth = filter_form.cleaned_data.get('max_depth')

			queryset = Product.objects.filter(
				Q(collection__in=filter_form.cleaned_data.get('collections')) |
				Q(fabric_name__product_fabric_color__color_name__in=filter_form.cleaned_data.get('colors')) |
				Q(category__type_ru__in=filter_form.cleaned_data.get('producttypes')) |
				Q(price__gte=min_price) |
				Q(price__lte=max_price) |
				Q(width__gte=min_width) |
				Q(width__lte=max_width) |
				Q(depth__gte=min_depth) |
				Q(depth__lte=max_depth)
			)
			products_list = queryset

	unique_product_type = Producttype.objects.values('type_ru').distinct()
	unique_color = Color.objects.values('color_name', 'color_id', 'color_code').distinct()
	unique_collection = Collection.objects.values('collection').annotate(total=Count('collection')).distinct()
	unique_paws_type = Product.objects.values('paws_type').annotate(total=Count('paws_type')).distinct()
	unique_mechanism_type = Product.objects.values('mechanism_type').distinct()

	# ADD PAGINATOR
	paginator = Paginator(products_list, 9)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	context = {
		'products': products,
		'products_list': products_list,
		'sort_by': sort_by,
		'filter_form': FilterForm(),
		'unique_product_type': unique_product_type,
		'unique_color': unique_color,
		'unique_mechanism_type': unique_mechanism_type,
		'unique_paws_type': unique_paws_type,
		'unique_collection': unique_collection,
	}
	
	return render(request, 'product/category_goods.html', context)


