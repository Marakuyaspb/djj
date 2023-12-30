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