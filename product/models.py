from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save
# from django.urls import reverse


class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_ru = models.CharField(max_length=50, verbose_name = 'Название категории (по-русски, в МНОЖЕСТВЕННОМ числе)')
	producttype = models.CharField(max_length=50, verbose_name = 'Название категории (то же, в ЕДИНСТВЕННОМ числе)')
	category = models.CharField(max_length=30, verbose_name='Сокращенно латиницей (arm, str, k1r и т.п.)')
	category_slug = models.SlugField(max_length=30, unique=True, verbose_name='Повторите')

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
	collection = models.CharField(max_length=30, verbose_name = 'Коллекция (Латиницей)')
	collection_slug = models.SlugField(max_length=30, unique=True, verbose_name='Повторите')

	class Meta:
		ordering = ['collection']
		indexes = [
		models.Index(fields=['collection']),
		]
		verbose_name = 'Коллекция'
		verbose_name_plural = 'Коллекции'
	def __str__(self):
		return self.collection

# class ProductType(models.Model):
# 	producttype_id = models.AutoField(primary_key=True)
# 	producttype = models.CharField(max_length=50) # Consono etc

# 	class Meta:
# 		ordering = ['producttype']
# 		indexes = [
# 		models.Index(fields=['producttype']),
# 		]
# 		verbose_name = 'Тип продукта'
# 		verbose_name_plural = 'Типы продуктов'
# 	def __str__(self):
# 		return self.producttype


class Fabric(models.Model):
	fabric_id = models.AutoField(primary_key=True)
	fabric_name = models.CharField(max_length=50, verbose_name = 'Название ткани')
	product_fabric_img = models.ImageField(upload_to='fabric_images/%Y/%m/%d', verbose_name = 'Образец ткани')
	product_fabric_about = models.CharField(max_length=1500, verbose_name = 'Описание ткани')
	created = models.DateTimeField(auto_now_add=True, verbose_name = 'Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name = 'Последние изменения')

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
	product_fabric_icon = models.ImageField(null=True, blank=True, upload_to='fabric_images/%Y/%m/%d', verbose_name = 'Иконка переключения ткани')
	product_fabric_name = models.CharField(null=True, blank=True, max_length=500, verbose_name = 'Название ткани')
	class Meta:
		ordering = ['product_fabric_name']
		indexes = [
		models.Index(fields=['product_fabric_name']),
		]
		verbose_name = 'Иконка переключения ткани'
		verbose_name_plural = 'Иконки переключения ткани'
	def __str__(self):
		return self.product_fabric_name


class Option(models.Model):
	option_id = models.AutoField(primary_key=True)
	option_name = models.CharField(max_length=350, null=True, blank=True, verbose_name = 'Заголовок опции (не обязательно)')
	option_1_img = models.ImageField(upload_to='options/%Y/%m/%d', verbose_name = 'Изображение 1')
	option_1_description = models.CharField(max_length=500, verbose_name = 'Описание опции 1')
	option_2_img = models.ImageField(upload_to='options/%Y/%m/%d', verbose_name = 'Изображение 2')
	option_2_description = models.CharField(max_length=500, verbose_name = 'Описание опции 2')
	created = models.DateTimeField(auto_now_add=True, verbose_name = 'Создано')
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
	created = models.DateTimeField(auto_now_add=True, verbose_name = 'Создано')
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


class SliderInterior(models.Model):
	slint_id = models.AutoField(primary_key=True)
	slint_name = models.CharField(max_length=350, verbose_name='Название слайдера')
	slint_img_1 = models.ImageField(upload_to='slider_interior/%Y/%m/%d', verbose_name = 'Десктоп | Изображение 1')
	slint_img_2 = models.ImageField(upload_to='slider_interior/%Y/%m/%d', verbose_name = 'Десктоп | Изображение 2')
	slint_img_3 = models.ImageField(upload_to='slider_interior/%Y/%m/%d', verbose_name = 'Десктоп | Изображение 3')
	slint_img_4 = models.ImageField(upload_to='slider_interior/%Y/%m/%d', verbose_name = 'Десктоп | Изображение 4')
	slint_img_mob_1 = models.ImageField(upload_to='slider_interior/%Y/%m/%d', verbose_name = 'Мобильный | Изображение 1')
	slint_img_mob_2 = models.ImageField(upload_to='slider_interior/%Y/%m/%d', verbose_name = 'Мобильный | Изображение 2')
	slint_img_mob_3 = models.ImageField(upload_to='slider_interior/%Y/%m/%d', verbose_name = 'Мобильный | Изображение 3')
	slint_img_mob_4 = models.ImageField(upload_to='slider_interior/%Y/%m/%d', verbose_name = 'Мобильный | Изображение 4')
	created = models.DateTimeField(auto_now_add=True, verbose_name = 'Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name = 'Последние изменения')

	class Meta:
		ordering = ['slint_name']
		indexes = [
		models.Index(fields=['slint_name']),
		]
		verbose_name = 'Слайдер с интерьерами'
		verbose_name_plural = 'Слайдеры с интерьерами'
	def __str__(self):
		return self.slint_name	


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
	product_img = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name = 'Изображение товара')
	# product_fabric_icon_1 = models.ImageField(upload_to='fabric_images/%Y/%m/%d', null=True, blank=True, verbose_name = '')
	# product_fabric_icon_2 = models.ImageField(upload_to='fabric_images/%Y/%m/%d', null=True, blank=True, verbose_name = '')
	# product_fabric_icon_3 = models.ImageField(upload_to='fabric_images/%Y/%m/%d', null=True, blank=True, verbose_name = '')
	# product_fabric_icon_4 = models.ImageField(upload_to='fabric_images/%Y/%m/%d', null=True, blank=True, verbose_name = '')
	# product_fabric_icon_5 = models.ImageField(upload_to='fabric_images/%Y/%m/%d', null=True, blank=True, verbose_name = '')
	product_fabric_icon_1 = models.ForeignKey(FabricIconChange,
		related_name='product_fabric_icon_1',
		on_delete=models.CASCADE, null=True, blank=True)
	product_fabric_icon_2 = models.ForeignKey(FabricIconChange,
		related_name='product_fabric_icon_2',
		on_delete=models.CASCADE, null=True, blank=True)
	product_fabric_icon_3 = models.ForeignKey(FabricIconChange,
		related_name='product_fabric_icon_3',
		on_delete=models.CASCADE, null=True, blank=True)
	product_fabric_icon_4 = models.ForeignKey(FabricIconChange,
		related_name='product_fabric_icon_4',
		on_delete=models.CASCADE, null=True, blank=True)
	product_fabric_icon_5 = models.ForeignKey(FabricIconChange,
		related_name='product_fabric_icon_5',
		on_delete=models.CASCADE, null=True, blank=True)
	show_on_category_page = models.BooleanField(default=True, verbose_name = 'Отображать в выдаче категории')
	popular = models.BooleanField(default=True, verbose_name = 'Отображать в карусели "Популярные"')
	is_new = models.BooleanField(default=True, verbose_name = 'Новый')
	available_for_delivery_2 = models.BooleanField(default=True, verbose_name = 'Доставим за 2 дня')
	available_for_delivery_28 = models.BooleanField(default=True, verbose_name = 'Доставим за 28 дней')
	available_in_showroom = models.BooleanField(default=True, verbose_name = 'Есть в шоуруме')
	# product_fabric_img = models.ImageField(upload_to='fabric_images/%Y/%m/%d', blank=True, verbose_name = 'Образец ткани')
	# product_fabric_about = models.CharField(max_length=1500, blank=True, verbose_name = 'Описание ткани')
	# product_fabric_icon = models.ManyToManyField(FabricIconChange, blank=True)
	description = models.CharField(max_length=1500, blank=True, verbose_name = 'Описание товара')
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = 'Цена')
	price_sale = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = 'Цена (распродажа)')
	carousel_items = models.ManyToManyField('ProductImage', related_name='carousel_items', blank=True)
	carousel_items_mob = models.ManyToManyField('ProductImage', related_name='carousel_items_mob', blank=True)
	closeup = models.ImageField(upload_to='closeups/', blank=True, verbose_name = 'Крупный фрагмент справа')
	slider_interior = models.ForeignKey(SliderInterior, verbose_name = 'Слайдер с интерьерами',
		related_name='products',
    	db_column='products',
		on_delete=models.CASCADE, null=True, blank=True)
	# slider_interior = models.ManyToManyField('ProductImage', related_name='slider_interior', blank=True)
	# slider_interior_mob = models.ManyToManyField('ProductImage', related_name='slider_interior_mob', blank=True)
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
	created = models.DateTimeField(auto_now_add=True, verbose_name = 'Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name = 'Последние изменения')
	product_slug = models.SlugField(max_length=100)

	
	class Meta:
		ordering = ['product_full_name']
		indexes = [
			models.Index(fields=['id', 'product_slug', '-created']),
			models.Index(fields=['product_full_name']),
			models.Index(fields=['-created']),
		]
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def save(self, *args, **kwargs):
		self.product_slug = slugify('-'.join([self.collection.collection, self.category.category, self.fabric_name.fabric_name]))
		super().save(*args, **kwargs)

	# def savecat(self, *args, **kwargs):
	# 	self.cat_slug = slugify('-'.join([self.category.category]))
	# 	super().save(*args, **kwargs)

	def __str__(self):
		return self.product_full_name



class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

		

class ProductImage(models.Model):
	image = models.ImageField(upload_to='product_images/%Y/%m/%d')
	caption = models.CharField(max_length=100, blank=True)
	def __str__(self):
		 return self.caption