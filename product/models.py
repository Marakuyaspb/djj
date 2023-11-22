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
	product_fabric_icon = models.ImageField(upload_to='fabric_images/%Y/')
	product_fabric_img = models.ImageField(upload_to='fabric_images/%Y/')
	product_fabric_about = models.ImageField(upload_to='fabric_images/%Y/')

	class Meta:
		ordering = ['fabric_name']
		indexes = [
		models.Index(fields=['fabric_name']),
		]
		verbose_name = 'Ткань'
		verbose_name_plural = 'Ткани'
	def __str__(self):
		return self.fabric_name		
		return self.product_fabric_icon
		return self.product_fabric_img
		return self.product_fabric_about


class Product(Category, Collection, Fabric):
	id = models.AutoField(primary_key=True)
	product_full_name = models.CharField(max_length=50) # Кресло Consono
	product_type = models.CharField(max_length=50) # Кресло
	product_img = models.CharField(max_length=150)
	popular = models.BooleanField(default=True)
	is_new = models.BooleanField(default=True)
	available_for_delivery_2 = models.BooleanField(default=True)
	available_for_delivery_28 = models.BooleanField(default=True)
	available_in_showroom = models.BooleanField(default=True)
	description = models.CharField(max_length=1500)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	price_sale = models.DecimalField(max_digits=10, decimal_places=2)
	carousel_items = models.ManyToManyField('ProductImage', related_name='carousel_items')	
	carousel_items_mob = models.ManyToManyField('ProductImage', related_name='carousel_items_mob')
	closeup = models.ImageField(upload_to='images/%Y/')
	slider_interior = models.ManyToManyField('ProductImage', related_name='slider_interior')
	slider_interior_mob = models.ManyToManyField('ProductImage', related_name='slider_interior_mob')
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
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=350)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)
	
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
		

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')