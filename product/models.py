from django.db import models
from django.conf import settings
from multiupload.fields import MultiFileField
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
# from django.urls import reverse


class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_ru = models.CharField(max_length=50, verbose_name = 'Название категории (по-русски, в МНОЖЕСТВЕННОМ числе)')
	producttype = models.CharField(max_length=50, null=True, verbose_name = 'Название категории (то же, в ЕДИНСТВЕННОМ числе)')
	category = models.CharField(max_length=30, verbose_name='Сокращенно латиницей (arm, str, k1r и т.п.)')
	category_slug = models.SlugField(max_length=30, unique=True, null=True, verbose_name='URL')

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
	collection = models.CharField(max_length=30, verbose_name = 'Коллекция (Латиницей, с большой буквы)')
	collection_slug = models.SlugField(max_length=30, unique=True, null=True, verbose_name='URL')

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
	fabric_name = models.CharField(max_length=50, verbose_name = 'Название ткани')
	product_fabric_img = models.ImageField(upload_to='fabric_images/%Y/%m/%d', verbose_name = 'Образец ткани')
	product_fabric_about = models.CharField(max_length=1500, verbose_name = 'Описание ткани')
	created = models.DateTimeField(default=timezone.now, verbose_name = 'Создано')
	updated = models.DateTimeField(default=timezone.now, verbose_name = 'Последние изменения')

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
	option_name = models.CharField(max_length=350, null=True, blank=True, verbose_name = 'Заголовок опции (не обязательно)')
	option_1_img = models.ImageField(upload_to='options/%Y/%m/%d', verbose_name = 'Изображение 1')
	option_1_description = models.CharField(max_length=500, verbose_name = 'Описание опции 1')
	option_2_img = models.ImageField(upload_to='options/%Y/%m/%d', verbose_name = 'Изображение 2')
	option_2_description = models.CharField(max_length=500, verbose_name = 'Описание опции 2')
	created = models.DateTimeField(default=timezone.now, verbose_name = 'Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name = 'Последние изменения')

	class Meta:
		ordering = ['option_name']
		indexes = [
		models.Index(fields=['option_name']),
		]
		verbose_name = 'Опция'
		verbose_name_plural = 'Опции'
	def __str__(self):
		return self.option_name	


class PopOverFeatures(models.Model):
	popover_id = models.AutoField(primary_key=True)
	popover_name = models.CharField(max_length=350, null=True, blank=True, verbose_name = 'Название фичи')
	popover_1_img = models.ImageField(upload_to='popover_features/%Y/%m/%d', verbose_name = 'Картинка фичи 1')
	popover_1_description = models.CharField(max_length=500, verbose_name = 'Описание фичи 1')
	popover_2_img = models.ImageField(upload_to='popover_features/%Y/%m/%d', verbose_name = 'Картинка фичи 2')
	popover_2_description = models.CharField(max_length=500, verbose_name = 'Описание фичи 2')
	popover_3_img = models.ImageField(upload_to='popover_features/%Y/%m/%d', verbose_name = 'Картинка фичи 3')
	popover_3_description = models.CharField(max_length=500, verbose_name = 'Описание фичи 3')
	popover_4_img = models.ImageField(upload_to='popover_features/%Y/%m/%d', verbose_name = 'Картинка фичи 4')
	popover_4_description = models.CharField(max_length=500, verbose_name = 'Описание фичи 4')
	popover_5_img = models.ImageField(upload_to='popover_features/%Y/%m/%d', verbose_name = 'Картинка фичи 5')
	popover_5_description = models.CharField(max_length=500, verbose_name = 'Описание фичи 5')
	created = models.DateTimeField(default=timezone.now, verbose_name = 'Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name = 'Последние изменения')

	class Meta:
		ordering = ['popover_name']
		indexes = [
		models.Index(fields=['popover_name']),
		]
		verbose_name = 'Фича поп-овер'
		verbose_name_plural = 'Фичи поп-овер'
	def __str__(self):
		return self.popover_name	


class Product(models.Model):
	id = models.AutoField(primary_key=True)
	category = models.ForeignKey(
		Category,
		related_name='products',
		on_delete=models.CASCADE, verbose_name = 'Категория')
	collection = models.ForeignKey(Collection,
		related_name='products',
		on_delete=models.CASCADE, verbose_name = 'Коллекция')
	fabric_name = models.ForeignKey(Fabric,
		related_name='products',
		on_delete=models.CASCADE, verbose_name = 'Название ткани')
	product_full_name = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Полное название товара (напр. Угловой диван Consono)')

	product_fabric_icon_1 = models.ImageField(upload_to='fabric_icons/%Y/%m/%d', default='fabric_icons/2023/12/06/CAMBRIDGE_600.png', null=True, blank=True, verbose_name = 'Иконка переключения ткани № 1')
	slug_fabric_icon_1 = models.SlugField(max_length=100, null=True, verbose_name='Название ткани №1')

	product_fabric_icon_2 = models.ImageField(upload_to='fabric_icons/%Y/%m/%d',  default='fabric_icons/2023/12/06/JAZZ_01.png', null=True, blank=True, verbose_name = 'Иконка переключения ткани № 2')
	slug_fabric_icon_2 = models.SlugField(max_length=100, null=True, verbose_name='Название ткани №2')

	product_fabric_icon_3 = models.ImageField(upload_to='fabric_icons/%Y/%m/%d', default='fabric_icons/2023/12/06/JAZZ_21.png', null=True, blank=True, verbose_name = 'Иконка переключения ткани № 3')
	slug_fabric_icon_3 = models.SlugField(max_length=100, null=True, verbose_name='Название ткани №3')

	product_fabric_icon_4 = models.ImageField(upload_to='fabric_icons/%Y/%m/%d', default='fabric_icons/2023/12/06/PIXEL_FOREST.png', null=True, blank=True, verbose_name = 'Иконка переключения ткани № 4')
	slug_fabric_icon_4 = models.SlugField(max_length=100, null=True, verbose_name='Название ткани №4')

	product_fabric_icon_5 = models.ImageField(upload_to='fabric_icons/%Y/%m/%d', default='fabric_icons/2023/12/06/VELUTTO_32.png', null=True, blank=True, verbose_name = 'Иконка переключения ткани № 5')
	slug_fabric_icon_5 = models.SlugField(max_length=100, null=True, verbose_name='Название ткани №5')
	
	show_on_category_page = models.BooleanField(default=True, verbose_name = 'Отображать в выдаче категории')

	popular = models.BooleanField(default=True, verbose_name = 'Отображать в карусели "Популярные"')

	is_new = models.BooleanField(default=True, verbose_name = 'Новый')
	available_for_delivery_2 = models.BooleanField(default=True, verbose_name = 'Доставим за 2 дня')
	available_for_delivery_28 = models.BooleanField(default=True, verbose_name = 'Доставим за 28 дней')
	available_in_showroom = models.BooleanField(default=True, verbose_name = 'Есть в шоуруме')
	icon_is_new = models.FileField(upload_to='status_icons/%Y/%m/%d', default='status_icons/2023/12/07/new.svg', null=True, blank=True, verbose_name = 'Иконка | Новый')
	icon_available_for_delivery_2 = models.FileField(upload_to='status_icons/%Y/%m/%d', default='status_icons/2023/12/07/delivery2.svg', null=True, blank=True, verbose_name = 'Иконка | Доставим за 2 дня')
	icon_available_for_delivery_28 = models.FileField(upload_to='status_icons/%Y/%m/%d', default='status_icons/2023/12/07/delivery2.svg', null=True, blank=True, verbose_name = 'Иконка | Доставим за 28 дней')
	icon_available_in_showroom =models.FileField(upload_to='status_icons/%Y/%m/%d', default='status_icons/2023/12/07/showrooms.svg',null=True, blank=True, verbose_name = 'Иконка | Есть в шоуруме')

	product_img = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True, verbose_name = 'Изображение товара')
	description = models.CharField(max_length=1500, null=True, blank=True, verbose_name = 'Описание товара')
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = 'Цена')
	price_sale = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = 'Цена (распродажа)')

	carousel_items = models.ManyToManyField('ProductImage', related_name='carousel_items', verbose_name ='Слайдер с товаром | десктоп')
	carousel_items_mob = models.ManyToManyField('ProductImage', related_name='carousel_items_mob', blank=True, verbose_name ='Слайдер с товаром | мобильный')
	closeup = models.ImageField(upload_to='closeups/', blank=True, null=True, verbose_name = 'Крупный фрагмент справа')
	interior_items = models.ManyToManyField('ProductImage', related_name='interior_items', blank=True, verbose_name ='Слайдер с интерьером | десктоп')
	interior_items_mob = models.ManyToManyField('ProductImage', related_name='interior_items_mob', blank=True, verbose_name ='Слайдер с интерьером | мобильный')
	width = models.IntegerField(blank=True, null=True, verbose_name = 'Ширина')
	depth = models.IntegerField(blank=True, null=True, verbose_name = 'Глубина')
	height = models.IntegerField(blank=True, null=True, verbose_name = 'Высота')
	pdf = models.CharField(max_length=150, null=True, blank=True, verbose_name = 'Файл PDF')
	product_inside = models.CharField(max_length=150, null=True, blank=True, verbose_name = 'Наполнение')
	product_inside_pillow = models.CharField(max_length=150, null=True, blank=True, verbose_name = 'Наполнение подушек')
	carcas_type = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Каркас')
	paws_type = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Ножки')
	mechanism_type = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Механизм')
	sleep_place = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Спальное место')
	linen_drawer = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Бельевой ящик')
	scheme = models.CharField(max_length=150, null=True, blank=True, verbose_name = 'Схема')
	options = models.ManyToManyField(Option, blank=True, verbose_name = 'Опции')
	features = models.CharField(max_length=350, null=True, blank=True, verbose_name = 'Конструктивные особенности')
	created = models.DateTimeField(default=timezone.now, verbose_name = 'Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name = 'Последние изменения')
	product_slug = models.SlugField(null=True, blank=True, max_length=100)

	
	class Meta:
		ordering = ['product_full_name']
		indexes = [
			models.Index(fields=['id', 'product_slug', '-created']),
			models.Index(fields=['product_full_name']),
			models.Index(fields=['-created']),
		]
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	#Category
	@property
	def category_slug(self):
		return self.category.category_slug

	#Collection
	@property
	def collection_slug(self):
		return self.collection.collection_slug

	# Fabric
	@property
	def fabric_img_url(self):
		return self.fabric_name.product_fabric_img.url
	@property
	def fabric_about(self):
		return self.fabric_name.product_fabric_about

	# Options
	@property
	def option_name(self):
		return self.options.option_name
	@property
	def option_1_img(self):
		return self.options.option_1_img
	@property
	def option_2_img(self):
		return self.options.option_2_img
	@property
	def option_1_description(self):
		return self.options.option_1_description
	@property
	def option_2_description(self):
		return self.options.option_2_description


	def save(self, *args, **kwargs):
		self.product_slug = slugify('-'.join([self.collection.collection, self.category.category, self.fabric_name.fabric_name]))
		super().save(*args, **kwargs)


	def __str__(self):
		return self.product_full_name

class ProductImage(models.Model):
	id = models.AutoField(primary_key=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	image = models.ImageField(upload_to='product_items/%Y/%m/%d')



class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)