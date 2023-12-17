from product.models import Product, Category


def only_objects_decorator(func: callable):
	def only_objects_wrapper(objects, only=(), *args, **kwargs):
		return func(objects, *args, **kwargs).only(*only)
	return only_objects_wrapper


@only_objects_decorator
def get_all_objects(objects):
	return objects.all()
	
@only_objects_decorator
def get_filter_objects(objects, category, **kwargs):
	return objects.filter(category=category, **kwargs)






###############################
# replace it to another file


def create_product(product_name: str):
	product_queryset = get_all_objects(Product.objects)
	get_filter_objects(product_queryset, category = 'arm')

def category_page_show():
	return only_objects(
		objects=get_all_objects(Product.objects),
		only=('product_slug', 'collection', 'is_new', 'available_in_showroom', 'available_for_delivery_2', 'product_img', 'price', 'price_sale', 'width', 'depth', 'height'))