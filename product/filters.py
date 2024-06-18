from django.db.models import Count, Q
from .models import Product, Collection, Color, Producttype

def product_ordering(instance, queryset, sort_by):
	if sort_by == 'asc':
		return queryset.order_by('price')
	elif sort_by == 'desc':
		return queryset.order_by('-price')
	else:
		return queryset


def product_filtering(request, queryset):
	filters = Q()

	min_price = (request.GET.get('min_price'))
	max_price = request.GET.get('max_price')
	min_width = request.GET.get('min_width')
	max_width = request.GET.get('max_width')
	min_depth = request.GET.get('min_depth')
	max_depth = request.GET.get('max_depth')
	collection_ids = request.GET.get('collection_id')
	color_ids = request.GET.get('color_id')
	type_ids = request.GET.get('type_id')
	paws_type = request.GET.get('paws_type')
	mechanism_type = request.GET.get('mechanism_type')
	linen_drawer = request.GET.get('linen_drawer')

	if min_price:
		filters &= Q(price__gte=min_price)
	if max_price:
		filters &= Q(price__lte=max_price)
	if min_width:
		filters &= Q(width__gte=min_width)
	if max_width:
		filters &= Q(width__lte=max_width)
	if min_depth:
		filters &= Q(depth__gte=min_depth)
	if max_depth:
		filters &= Q(depth__lte=max_depth)
	if collection_ids:
		filters &= Q(collection_id__in=collection_ids)
	if color_ids:
		filters &= Q(fabric_name__product_fabric_color__color_id__in=color_ids)
	if type_ids:
		filters &= Q(category__type_ru__type_id__in=type_ids)
	if paws_type:
		filters &= Q(paws_type=paws_type)
	if mechanism_type:
		filters &= Q(mechanism_type=mechanism_type)
	if linen_drawer:
		filters &= Q(linen_drawer=linen_drawer)

	return queryset.filter(filters)

def unique_names(request):
	unique_product_type = Producttype.objects.values('type_ru', 'type_id').distinct()
	unique_color = Color.objects.values('color_name', 'color_id', 'color_code').distinct()
	unique_collection = Collection.objects.values('collection', 'collection_id').distinct()
	unique_paws_type = Product.objects.values('paws_type').annotate(total=Count('paws_type')).order_by('paws_type').distinct()
	unique_mechanism_type = Product.objects.values('mechanism_type').annotate(total=Count('mechanism_type')).order_by('mechanism_type').distinct()
	print(unique_collection)
	return {
		'unique_product_type': unique_product_type,
		'unique_color': unique_color,
		'unique_collection': unique_collection,
		'unique_paws_type': unique_paws_type,
		'unique_mechanism_type': unique_mechanism_type,
	}