from django.db import models
from django.conf import settings
from django.utils.text import slugify
# from django.urls import reverse


class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category = models.CharField(max_length=50) # КреслА, пуфЫ etc
	category_ru = models.CharField(max_length=50)
	slug = models.SlugField(max_length=200,
                            unique=True)

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
	product_fabric_img = models.ImageField(upload_to='fabric_images/%Y/%m/%d')
	product_fabric_about = models.CharField(max_length=1500)

	class Meta:
		ordering = ['fabric_name']
		indexes = [
		models.Index(fields=['fabric_name']),
		]
		verbose_name = 'Ткань'
		verbose_name_plural = 'Ткани'
	def __str__(self):
		return self.fabric_name	



class FabricIconChange(models.Model):
	fabric_icon_id = models.AutoField(primary_key=True)
	product_fabric_icon = models.ImageField(upload_to='fabric_images/%Y/%m/%d')
	product_fabric_name = models.CharField(max_length=50, null=True, blank=True)
	class Meta:
		ordering = ['product_fabric_name']
		indexes = [
		models.Index(fields=['product_fabric_icon']),
		]
		verbose_name = 'Иконка переключения ткани'
		verbose_name_plural = 'Иконки переключения ткани'
	def __str__(self):
		return self.product_fabric_name


class Option(models.Model):
	option_id = models.AutoField(primary_key=True)
	option_name = models.CharField(max_length=350, null=True, blank=True)
	option_1_img = models.ImageField(upload_to='options/%Y/%m/%d')
	option_1_description = models.CharField(max_length=500)
	option_2_img = models.ImageField(upload_to='options/%Y/%m/%d')
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
	category = models.ForeignKey(
		Category,
		related_name='products',
		on_delete=models.CASCADE)
	collection = models.ForeignKey(Collection,
		related_name='products',
		on_delete=models.CASCADE)
	product_full_name = models.CharField(max_length=50, null=True, blank=True) # Кресло Consono
	product_type = models.CharField(max_length=50, null=True, blank=True) # Кресло
	product_img = models.ImageField(upload_to='images/%Y/%m/%d', blank=True
		)
	popular = models.BooleanField(default=True)
	is_new = models.BooleanField(default=True)
	available_for_delivery_2 = models.BooleanField(default=True)
	available_for_delivery_28 = models.BooleanField(default=True)
	available_in_showroom = models.BooleanField(default=True)
	fabric_name = models.ForeignKey(Fabric,
		related_name='products',
    	db_column='products',
		on_delete=models.CASCADE)
	product_fabric_icon = models.ManyToManyField(FabricIconChange, blank=True)
	description = models.CharField(max_length=1500, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	price_sale = models.DecimalField(max_digits=10, decimal_places=2)
	carousel_items = models.ManyToManyField('ProductImage', related_name='carousel_items', blank=True)	
	carousel_items_mob = models.ManyToManyField('ProductImage', related_name='carousel_items_mob', blank=True)
	closeup = models.ImageField(upload_to='closeups/', blank=True)
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
	options = models.ManyToManyField(Option, blank=True)
	features = models.CharField(max_length=350, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=350, default='pr')

	# def display_options(self):
	# 	return ', '.join([str(option.option_name) 
	# 		for option in self.options.all()])
	
	class Meta:
		ordering = ['product_full_name']
		indexes = [
			models.Index(fields=['id', 'slug', '-created']),
			models.Index(fields=['product_full_name']),
			models.Index(fields=['-created']),
		]
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.product_full_name


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

		

class ProductImage(models.Model):
	image = models.ImageField(upload_to='product_images/')
	def __str__(self):
		return self.image