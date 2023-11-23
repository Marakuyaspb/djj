from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category = models.CharField(max_length=50) # КреслА, пуфЫ etc
	category_ru = models.CharField(max_length=50)

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
	collection_id = models.AutoField(primary_key=True)
	collection = models.CharField(max_length=50) # Consono etc

	class Meta:
		ordering = ['collection']
		indexes = [
		models.Index(fields=['collection']),
		]
		verbose_name = 'Коллекция'
		verbose_name_plural = 'Коллекции'
	def __str__(self):
		return self.collection


class Fabric(models.Model):
	fabric_id = models.AutoField(primary_key=True)
	fabric_name = models.CharField(max_length=50)
	product_fabric_icon = models.ImageField(upload_to='fabric_images/')
	product_fabric_img = models.ImageField(upload_to='fabric_images/')
	product_fabric_about = models.CharField(max_length=1500)
	# slug = models.SlugField(max_length=350)

	class Meta:
		ordering = ['fabric_name']
		indexes = [
		models.Index(fields=['fabric_name']),
		]
		verbose_name = 'Ткань'
		verbose_name_plural = 'Ткани'
	def __str__(self):
		return self.fabric_name		


class Option(models.Model):
	option_id = models.AutoField(primary_key=True)
	option_name = models.CharField(max_length=350, null=True, blank=True)
	option_1_img = models.ImageField(upload_to='options/')
	option_1_description = models.CharField(max_length=500)
	option_2_img = models.ImageField(upload_to='options/')
	option_2_description = models.CharField(max_length=500)

	class Meta:
		ordering = ['option_name']
		indexes = [
		models.Index(fields=['option_name']),
		]
		verbose_name = 'Опция'
		verbose_name_plural = 'Опции'
	def __str__(self):
		return self.option_name		


class Product(models.Model):
	id = models.AutoField(primary_key=True)
	product_full_name = models.CharField(max_length=50, null=True, blank=True) # Кресло Consono
	product_type = models.CharField(max_length=50, null=True, blank=True) # Кресло
	product_img = models.ImageField(upload_to='images/', null=True, blank=True)
	popular = models.BooleanField(default=True)
	is_new = models.BooleanField(default=True)
	available_for_delivery_2 = models.BooleanField(default=True)
	available_for_delivery_28 = models.BooleanField(default=True)
	available_in_showroom = models.BooleanField(default=True)
	fabric_current = models.ForeignKey(Fabric,
		related_name='fabric_current',
    	db_column='fabric_current',
		on_delete=models.CASCADE)
	fabric = models.ManyToManyField(Fabric,
		related_name='fabric_icons',
    	db_column='fabric_icons',)
	# fabric_1 = models.ManyToManyField(Fabric)
	# fabric_2 = models.ManyToManyField(Fabric)
	# fabric_3 = models.ManyToManyField(Fabric)
	# fabric_4 = models.ManyToManyField(Fabric)
	# fabric_5 = models.ManyToManyField(Fabric)
	description = models.CharField(max_length=1500, null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	price_sale = models.DecimalField(max_digits=10, decimal_places=2)
	carousel_items = models.ManyToManyField('ProductImage', related_name='carousel_items', blank=True)	
	carousel_items_mob = models.ManyToManyField('ProductImage', related_name='carousel_items_mob', blank=True)
	closeup = models.ImageField(upload_to='closeups/', null=True, blank=True)
	slider_interior = models.ManyToManyField('ProductImage', related_name='slider_interior', blank=True)
	slider_interior_mob = models.ManyToManyField('ProductImage', related_name='slider_interior_mob', blank=True)
	width = models.IntegerField(blank=True, null=True)
	depth = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)
	pdf = models.CharField(max_length=150, null=True, blank=True)
	product_inside = models.CharField(max_length=150, null=True, blank=True)
	product_inside_pillow = models.CharField(max_length=150, null=True, blank=True)
	carcas_type = models.CharField(max_length=50, null=True, blank=True)
	paws_type = models.CharField(max_length=50, null=True, blank=True)
	mechanism_type = models.CharField(max_length=50, null=True, blank=True)
	sleep_place = models.CharField(max_length=50, null=True, blank=True)
	linen_drawer = models.CharField(max_length=50, null=True, blank=True)
	scheme = models.CharField(max_length=150, null=True, blank=True)
	option = models.ForeignKey(Option, default=1, on_delete=models.CASCADE)
	features = models.CharField(max_length=350, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=350)

	# def save(self, *args, **kwargs):
	# 	if not self.slug:
	# 		self.slug = slugify(self.title)
	# 	super().save(*args, **kwargs)
	
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
		

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')