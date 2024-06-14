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