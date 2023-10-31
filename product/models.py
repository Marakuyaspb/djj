from django.db import models
from django.conf import settings

class Category(models.Model):
	category = models.CharField(max_length=50) # КреслА, пуфЫ etc
	slug = models.SlugField(max_length=50, unique=True)

	class Meta:
		ordering = ['category']
		indexes = [
		models.Index(fields=['category']),
		]
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
	def __str__(self):
		return self.category


class Collection(models.Model):
	collection = models.CharField(max_length=50) # Consono etc
	slug = models.SlugField(max_length=50, unique=True)

	class Meta:
		ordering = ['collection']
		indexes = [
		models.Index(fields=['collection']),
		]
		verbose_name = 'Коллекция'
		verbose_name_plural = 'Коллекции'
	def __str__(self):
		return self.collection


class Product(models.Model):
	collection = models.CharField(max_length=50) # Consono
	category = models.ForeignKey(Category,
		related_name='products',
		on_delete=models.CASCADE)
	category_ru = models.CharField(max_length=50)
	product_full_name = models.CharField(max_length=50) # Кресло Consono
	product_type = models.CharField(max_length=50) # Кресло
	product_img = models.CharField(max_length=150)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	price_sale = models.DecimalField(max_digits=10, decimal_places=2)
	fabric_type = models.CharField(max_length=50)
	fabric_name = models.CharField(max_length=50)
	product_fabric_about = models.CharField(max_length=700)
	product_fabric_img = models.CharField(max_length=150)
	carousel_item_1 = models.CharField(max_length=150)
	carousel_item_2 = models.CharField(max_length=150)
	carousel_item_3 = models.CharField(max_length=150)
	carousel_item_4 = models.CharField(max_length=150)
	carousel_item_5 = models.CharField(max_length=150)
	carousel_item_mob_1 = models.CharField(max_length=150)
	carousel_item_mob_2 = models.CharField(max_length=150)
	carousel_item_mob_3 = models.CharField(max_length=150)
	carousel_item_mob_4 = models.CharField(max_length=150)
	carousel_item_mob_5 = models.CharField(max_length=150)
	closeup = models.CharField(max_length=150)
	slider_interior_1 = models.CharField(max_length=150)
	slider_interior_2 = models.CharField(max_length=150)
	slider_interior_3 = models.CharField(max_length=150)
	slider_interior_4 = models.CharField(max_length=150)
	slider_interior_1_mob = models.CharField(max_length=150)
	slider_interior_2_mob = models.CharField(max_length=150)
	slider_interior_3_mob = models.CharField(max_length=150)
	slider_interior_4_mob = models.CharField(max_length=150)
	width = models.IntegerField(blank=True, null=True)
	depth = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)
	pdf = models.CharField(max_length=150)
	product_inside = models.CharField(max_length=150)
	product_inside_pillow = models.CharField(max_length=150)
	carcas_type = models.CharField(max_length=50)
	paws_type = models.CharField(max_length=50)
	mechanism_type = models.CharField(max_length=50)
	sleep_place = models.CharField(max_length=50)
	linen_drawer = models.CharField(max_length=50)
	scheme = models.CharField(max_length=150)
	features = models.CharField(max_length=350)
	is_new = models.BooleanField(default=True)
	available_for_delivery_2 = models.BooleanField(default=True)
	available_for_delivery_28 = models.BooleanField(default=True)
	available_in_showroom = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=250)

	#scheme = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
	# image = models.FilePathField(path="/product/static", match="foo.*", recursive=True)
	# is_new = models.BooleanField(default=True)
	# available_for_delivery_2 = models.BooleanField(default=True)
	# available_for_delivery_28 = models.BooleanField(default=True)
	# available_in_showroom = models.BooleanField(default=True)
	# product_fabric_img = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
	# carousel_item = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
	# carousel_item_mob = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
	# closeup = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
	# slider_interior = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
	# slider_interior_mob = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
	
	
	class Meta:
		ordering = ['product_full_name']
		indexes = [
			models.Index(fields=['id', 'slug']),
			models.Index(fields=['product_full_name']),
			models.Index(fields=['-created']),
		]
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.product_full_name
		return self.price
		return self.price_sale
		return self.prod_width
		return self.prod_depth
		return self.prod_height
		
