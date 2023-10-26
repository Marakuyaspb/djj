from django.db import models

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
	name = models.CharField(max_length=50) # Кресло Consono
	product_type = models.CharField(max_length=50) # Кресло
	image = models.ImageField(upload_to='products/%Y/%m/%d',
	blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	price_sale = models.DecimalField(max_digits=10, decimal_places=2)
	is_new = models.BooleanField(default=True)
	available_for_delivery_2 = models.BooleanField(default=True)
	available_for_delivery_28 = models.BooleanField(default=True)
	available_in_showroom = models.BooleanField(default=True)
	fabric_type = models.CharField(max_length=50)
	fabric_name = models.CharField(max_length=50)
	product_fabric_about = models.CharField(max_length=700)
	#product_fabric_img = models.FilePathField(path=images_path)
	#carousel_item = models.FilePathField(path=images_path)
	#carousel_item_mob = models.FilePathField(path=images_path)
	#closeup = models.FilePathField(path=images_path)
	#slider_interior = models.FilePathField(path=images_path)
	#slider_interior_mob = models.FilePathField(path=images_path)
	prod_width = models.IntegerField(blank=True, null=True)
	prod_depth = models.IntegerField(blank=True, null=True)
	prod_height = models.IntegerField(blank=True, null=True)
	#scheme = models.FilePathField(path=images_path)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=250)
	
	class Meta:
		ordering = ['name']
		indexes = [
			models.Index(fields=['id', 'slug']),
			models.Index(fields=['name']),
			models.Index(fields=['-created']),
		]
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.name
		return self.price
		return self.price_sale
		return self.prod_width
		return self.prod_depth
		return self.prod_height
		
