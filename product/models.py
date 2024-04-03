from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings

from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

#from multiupload.fields import MultiFileField


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
	product_fabric_img = models.ImageField(upload_to='fabric_images/', verbose_name = 'Образец ткани')
	product_fabric_about = models.TextField(verbose_name = 'Описание ткани')
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
	option_1_img = models.ImageField(upload_to='options/', verbose_name = 'Изображение 1')
	option_1_description = models.CharField(max_length=500, null=True, blank=True, verbose_name = 'Описание опции 1')
	option_2_img = models.ImageField(upload_to='options/', verbose_name = 'Изображение 2')
	option_2_description = models.CharField(max_length=500, null=True, blank=True, verbose_name = 'Описание опции 2')
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


class SliderInterior(models.Model):
	sl_interior_id = models.AutoField(primary_key=True)
	sl_interior_name = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Название слайдера (коллекция)')
	sl_interior_1_img = models.ImageField(upload_to='interiors/', verbose_name = 'Изображение 1 | десктоп')
	sl_interior_2_img = models.ImageField(upload_to='interiors/', verbose_name = 'Изображение 2 | десктоп')
	sl_interior_3_img = models.ImageField(upload_to='interiors/', verbose_name = 'Изображение 3 | десктоп')
	sl_interior_4_img = models.ImageField(upload_to='interiors/', verbose_name = 'Изображение 4 | десктоп')
	sl_interior_1_img_mob = models.ImageField(upload_to='interiors/', verbose_name = 'Изображение 1 | мобильный')
	sl_interior_2_img_mob = models.ImageField(upload_to='interiors/', verbose_name = 'Изображение 2 | мобильный')
	sl_interior_3_img_mob = models.ImageField(upload_to='interiors/', verbose_name = 'Изображение 3 | мобильный')
	sl_interior_4_img_mob = models.ImageField(upload_to='interiors/', verbose_name = 'Изображение 4 | мобильный')
	created = models.DateTimeField(default=timezone.now, verbose_name = 'Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name = 'Последние изменения')

	class Meta:
		ordering = ['sl_interior_name']
		indexes = [
		models.Index(fields=['sl_interior_name']),
		]
		verbose_name = 'Слайдер с интерьерами'
		verbose_name_plural = 'Слайдеры с интерьерами'
	def __str__(self):
		return self.sl_interior_name	


class PopOverFeatures(models.Model):
	popover_id = models.AutoField(primary_key=True)
	popover_name = models.CharField(max_length=350, null=True, blank=True, verbose_name = 'Название набора 5 фич')
	category = models.ForeignKey(
		Category,
		related_name='features', default='1',
		on_delete=models.CASCADE, verbose_name = 'Категория')
	collection = models.ForeignKey(Collection,
		related_name='features', default='1',
		on_delete=models.CASCADE, verbose_name = 'Коллекция')
	popover_1_img = models.ImageField(upload_to='popover_features/', verbose_name = 'Картинка фичи 1')
	popover_1_description = models.CharField(max_length=500, verbose_name = 'Описание фичи 1')
	popover_2_img = models.ImageField(upload_to='popover_features/', verbose_name = 'Картинка фичи 2')
	popover_2_description = models.CharField(max_length=500, verbose_name = 'Описание фичи 2')
	popover_3_img = models.ImageField(upload_to='popover_features/', verbose_name = 'Картинка фичи 3')
	popover_3_description = models.CharField(max_length=500, verbose_name = 'Описание фичи 3')
	popover_4_img = models.ImageField(upload_to='popover_features/', verbose_name = 'Картинка фичи 4')
	popover_4_description = models.CharField(max_length=500, verbose_name = 'Описание фичи 4')
	popover_5_img = models.ImageField(upload_to='popover_features/', verbose_name = 'Картинка фичи 5')
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



class Schemes(models.Model):
	scheme_id = models.AutoField(primary_key=True)
	scheme_name = models.CharField(max_length=50, verbose_name = 'Название (для какой коллекции/модели?)')
	scheme_1 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 1')
	scheme_2 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 2')
	scheme_3 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 3')
	scheme_4 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 4')
	scheme_5 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 5')
	scheme_6 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 6')
	scheme_7 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 7')
	scheme_8 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 8')
	scheme_9 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 9')
	scheme_10 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 10')
	scheme_11 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 11')
	scheme_12 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 12')
	scheme_13 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 13')
	scheme_14 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 14')
	scheme_15 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 15')
	scheme_16 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 16')
	scheme_17 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 17')
	scheme_18 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 18')
	scheme_19 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 19')
	scheme_20 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 20')
	scheme_21 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 21')
	scheme_22 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 22')
	scheme_23 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 23')
	scheme_24 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 24')
	scheme_25 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 25')
	scheme_26 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 26')
	scheme_27 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 27')
	scheme_28 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 28')
	scheme_29 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 29')
	scheme_30 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 30')
	scheme_31 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 31')
	scheme_32 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 32')
	scheme_33 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 33')
	scheme_34 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 34')
	scheme_35 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 35')
	scheme_36 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 36')
	scheme_37 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 37')
	scheme_38 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 38')
	scheme_39 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 39')
	scheme_40 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 40')
	scheme_41 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 41')
	scheme_42 = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема 42')
		
	class Meta:
		ordering = ['scheme_name']
		indexes = [
		models.Index(fields=['scheme_name']),
		]
		verbose_name = 'Схему товара'
		verbose_name_plural = 'Схемы товаров SVG'
	def __str__(self):
		return self.scheme_name	




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
	product_full_name = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Полное название товара')
	product_img = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name = 'Изображение для страницы выдачи | десктоп')
	product_img_mob = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name = 'Изображение для страницы выдачи | мобильный')


	show_fabric_icons = models.BooleanField(default=True, verbose_name = 'Отображать иконки переключения тканей?')


	slug_fabric_icon_1 = models.SlugField(max_length=100, null=True, blank=True, verbose_name='Слаг ткани №1', default='cambridge-600')
	product_fabric_icon_1 = models.ImageField(upload_to='fabric_icons/', null=True, blank=True, verbose_name = 'Иконка переключения ткани № 1', default='fabric_icons/2024/01/23/CAMBRIDGE_600.png')
	
	slug_fabric_icon_2 = models.SlugField(max_length=100, null=True, blank=True, verbose_name='Слаг ткани №2', default='jazz-01')
	product_fabric_icon_2 = models.ImageField(upload_to='fabric_icons/', null=True, blank=True, verbose_name = 'Иконка переключения ткани № 2', default='fabric_icons/2024/01/23/JAZZ_01.png')

	slug_fabric_icon_3 = models.SlugField(max_length=100, null=True, blank=True, verbose_name='Слаг ткани №3', default='jazz-21')
	product_fabric_icon_3 = models.ImageField(upload_to='fabric_icons/', null=True, blank=True, verbose_name = 'Иконка переключения ткани № 3', default='fabric_icons/2024/01/23/JAZZ_21.png')

	slug_fabric_icon_4 = models.SlugField(max_length=100, null=True, blank=True, verbose_name='Слаг ткани №4', default='pixel-forest')
	product_fabric_icon_4 = models.ImageField(upload_to='fabric_icons/', null=True, blank=True, verbose_name = 'Иконка переключения ткани № 4', default='fabric_icons/2024/01/23/PIXEL_FOREST.png')
	
	slug_fabric_icon_5 = models.SlugField(max_length=100, null=True, blank=True, verbose_name='Слаг ткани №5', default='velutto-32')
	product_fabric_icon_5 = models.ImageField(upload_to='fabric_icons/', null=True, blank=True, verbose_name = 'Иконка переключения ткани № 5', default='fabric_icons/2024/01/23/VELUTTO_32.png')
	
	price = models.IntegerField(blank=True, null=True, verbose_name = 'Цена')
	price_old = models.IntegerField(blank=True, null=True, verbose_name = 'Старая цена')
	
	description = models.TextField(null=True, blank=True, verbose_name = 'Описание товара')


# Carousel #
	carousel_item_1 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 1 | десктоп', default='static/img/popovers_arm.png', null=True, blank=True)
	carousel_item_2 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 2 | десктоп', default='static/img/popovers_arm.png', null=True, blank=True)
	carousel_item_3 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 3 | десктоп', default='static/img/popovers_arm.png', null=True, blank=True)
	carousel_item_4 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 4 | десктоп', default='static/img/popovers_arm.png', null=True, blank=True)
	carousel_item_5 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 5 | десктоп', default='static/img/popovers_arm.png', null=True, blank=True)
	carousel_item_6 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 6 | десктоп', default='static/img/popovers_arm.png', null=True, blank=True)
	carousel_item_mob_1 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 1 | мобильный', default='static/img/popovers_arm.png', null=True, blank=True)
	carousel_item_mob_2 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 2 | мобильный', default='static/img/popovers_arm.png', null=True, blank=True)
	carousel_item_mob_3 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 3 | мобильный', default='static/img/popovers_arm.png', null=True, blank=True)
	carousel_item_mob_4 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 4 | мобильный', default='static/img/popovers_arm.png', null=True, blank=True)
	carousel_item_mob_5 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 5 | мобильный', default='static/img/popovers_arm.png', null=True, blank=True)
	carousel_item_mob_6 = models.ImageField(upload_to='carousel/', verbose_name = 'Изображение 6 | мобильный', default='static/img/popovers_arm.png', null=True, blank=True)

	closeup = models.ImageField(upload_to='closeups/', blank=True, null=True, verbose_name = 'Крупный фрагмент справа')

	width = models.IntegerField(blank=True, null=True, verbose_name = 'Ширина')
	depth = models.IntegerField(blank=True, null=True, verbose_name = 'Глубина')
	height = models.IntegerField(blank=True, null=True, verbose_name = 'Высота')
	
	product_inside = models.CharField(max_length=150, null=True, blank=True, verbose_name = 'Наполнение')
	product_inside_pillow = models.CharField(max_length=150, null=True, blank=True, verbose_name = 'Наполнение подушек')
	carcas_type = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Каркас')
	paws_type = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Ножки')
	mechanism_type = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Механизм')
	sleep_place = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Спальное место')
	linen_drawer = models.CharField(max_length=50, null=True, blank=True, verbose_name = 'Бельевой ящик')
	features = models.TextField(null=True, blank=True, verbose_name = 'Конструктивные особенности')
	
	pdf =  models.FileField(upload_to='pdf/', null=True, blank=True, verbose_name = 'Файл PDF')
	d3 =  models.FileField(upload_to='3d/', null=True, blank=True, verbose_name = 'Файл 3D-модели')
	# scheme = models.FileField(upload_to='schemes/', null=True, blank=True, verbose_name = 'Схема')
	scheme = models.ForeignKey(Schemes, blank=True, null=True, on_delete=models.CASCADE, verbose_name = 'Набор схем товара')


	options = models.ManyToManyField(Option, verbose_name = 'Опции', blank=True)

	slider_interior = models.ForeignKey(SliderInterior, blank=True, null=True,on_delete=models.CASCADE, verbose_name = 'Слайдер с интерьерами')
	popover = models.ForeignKey(PopOverFeatures, blank=True, null=True, on_delete=models.CASCADE, verbose_name = 'Поповер фичи')
	popover_img = models.ImageField(upload_to='popovers/', blank=True, null=True, verbose_name = 'Фоновая картинка')


	is_new = models.BooleanField(default=True, verbose_name = 'Новый')
	available_for_delivery_2 = models.BooleanField(default=False, verbose_name = 'Доставим за 2 дня')
	available_for_delivery_28 = models.BooleanField(default=True, verbose_name = 'Доставим за 28 дней')
	available_in_showroom = models.BooleanField(default=False, verbose_name = 'Есть в шоуруме')

	show_on_category_page = models.BooleanField(default=True, verbose_name = 'На страницу категории')
	popular = models.BooleanField(default=True, verbose_name = 'В карусель "Популярные"')

	created = models.DateTimeField(default=timezone.now, verbose_name = 'Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name = 'Посл. изменения')
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
	@property
	def category_ru(self):
		return self.category.category_ru


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

	#Slider interiors
	@property
	def sl_interior_name(self):
		return self.slider_interior.sl_interior_name
	@property
	def sl_interior_1_img(self):
		return self.slider_interior.sl_interior_1_img
	@property
	def sl_interior_2_img(self):
		return self.slider_interior.sl_interior_2_img
	@property
	def sl_interior_3_img(self):
		return self.slider_interior.sl_interior_3_img
	@property
	def sl_interior_4_img(self):
		return self.slider_interior.sl_interior_4_img
	@property
	def sl_interior_1_img_mob(self):
		return self.slider_interior.sl_interior_1_img_mob
	@property
	def sl_interior_2_img_mob(self):
		return self.slider_interior.sl_interior_2_img_mob
	@property
	def sl_interior_3_img_mob(self):
		return self.slider_interior.sl_interior_3_img_mob
	@property
	def sl_interior_4_img_mob(self):
		return self.slider_interior.sl_interior_4_img_mob


	#PopOverFeatures
	@property
	def popover_name(self):
		return self.popover.popover_name
	@property
	def popover_1_img(self):
		return self.popover.popover_1_img
	@property
	def popover_1_description(self):
		return self.popover.popover_1_description
	@property
	def popover_2_img(self):
		return self.popover.popover_2_img
	@property
	def popover_2_description(self):
		return self.popover.popover_2_description
	@property
	def popover_3_img(self):
		return self.popover.popover_3_img
	@property
	def popover_3_description(self):
		return self.popover.popover_3_description
	@property
	def popover_4_img(self):
		return self.popover.popover_4_img
	@property
	def popover_4_description(self):
		return self.popover.popover_4_description
	@property
	def popover_5_img(self):
		return self.popover.popover_5_img
	@property
	def popover_5_description(self):
		return self.popover.popover_5_description

	#Schemes
	@property
	def scheme_name(self):
		return self.scheme.scheme_name
	@property
	def scheme_1(self):
		return self.scheme.scheme_1
	@property
	def scheme_2(self):
		return self.scheme.scheme_2
	@property
	def scheme_3(self):
		return self.scheme.scheme_3
	@property
	def scheme_4(self):
		return self.scheme.scheme_4
	@property
	def scheme_5(self):
		return self.scheme.scheme_5
	@property
	def scheme_6(self):
		return self.scheme.scheme_6
	@property
	def scheme_7(self):
		return self.scheme.scheme_7
	@property
	def scheme_8(self):
		return self.scheme.scheme_8
	@property
	def scheme_9(self):
		return self.scheme.scheme_9
	@property
	def scheme_10(self):
		return self.scheme.scheme_10
	@property
	def scheme_11(self):
		return self.scheme.scheme_11
	@property
	def scheme_12(self):
		return self.scheme.scheme_12
	@property
	def scheme_13(self):
		return self.scheme.scheme_13
	@property
	def scheme_14(self):
		return self.scheme.scheme_14
	@property
	def scheme_15(self):
		return self.scheme.scheme_15
	@property
	def scheme_16(self):
		return self.scheme.scheme_16
	@property
	def scheme_17(self):
		return self.scheme.scheme_17
	@property
	def scheme_18(self):
		return self.scheme.scheme_18
	@property
	def scheme_19(self):
		return self.scheme.scheme_19
	@property
	def scheme_20(self):
		return self.scheme.scheme_20
	@property
	def scheme_21(self):
		return self.scheme.scheme_21
	@property
	def scheme_22(self):
		return self.scheme.scheme_22
	@property
	def scheme_23(self):
		return self.scheme.scheme_23
	@property
	def scheme_24(self):
		return self.scheme.scheme_24
	@property
	def scheme_25(self):
		return self.scheme.scheme_25
	@property
	def scheme_26(self):
		return self.scheme.scheme_26
	@property
	def scheme_27(self):
		return self.scheme.scheme_27
	@property
	def scheme_28(self):
		return self.scheme.scheme_28
	@property
	def scheme_29(self):
		return self.scheme.scheme_29
	@property
	def scheme_30(self):
		return self.scheme.scheme_30
	@property
	def scheme_31(self):
		return self.scheme.scheme_31
	@property
	def scheme_32(self):
		return self.scheme.scheme_32
	@property
	def scheme_33(self):
		return self.scheme.scheme_33
	@property
	def scheme_34(self):
		return self.scheme.scheme_34
	@property
	def scheme_35(self):
		return self.scheme.scheme_35
	@property
	def scheme_36(self):
		return self.scheme.scheme_36
	@property
	def scheme_37(self):
		return self.scheme.scheme_37
	@property
	def scheme_38(self):
		return self.scheme.scheme_38
	@property
	def scheme_39(self):
		return self.scheme.scheme_39
	@property
	def scheme_40(self):
		return self.scheme.scheme_40
	@property
	def scheme_41(self):
		return self.scheme.scheme_41
	@property
	def scheme_42(self):
		return self.scheme.scheme_42	


	def save(self, *args, **kwargs):
		self.product_slug = slugify('-'.join([self.collection.collection, self.category.category, self.fabric_name.fabric_name]))
		super().save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse('single_product', kwargs={'product_slug': self.product_slug})

	def __str__(self):
		#return self.product_full_name
		return f"Product: {self.id}, Options: {', '.join([str(option) for option in self.options.all()])}"


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)



class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='images')
	image = models.ImageField(upload_to='product_items/%Y/%m/%d')
