from django.contrib import admin
from .models import Category, Collection, Option, Fabric, SliderInterior, Product, ProductImage, PopOverFeatures
from django.utils.safestring import mark_safe
# from .forms import ProductImageForm
from django.template.loader import get_template
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.forms import CheckboxSelectMultiple



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	
	list_display = ('product_full_name', 'get_html_img_preview', 'fabric_name', 'price', 'price_old', 'popular', 'is_new', 'available_in_showroom', 'created', 'updated') 

	fields = ['category', 'collection', 
		'fabric_name', 
		'product_img', 		
		'product_full_name', 
		('slug_fabric_icon_1', 'product_fabric_icon_1'),
		('slug_fabric_icon_2', 'product_fabric_icon_2'),
		('slug_fabric_icon_3', 'product_fabric_icon_3'),
		('slug_fabric_icon_4', 'product_fabric_icon_4'),
		('slug_fabric_icon_5', 'product_fabric_icon_5'),
		'price', 
		'price_old', 
		'description', 
		('carousel_item_1', 'carousel_item_2', 'carousel_item_3', 'carousel_item_4', 'carousel_item_5'),
		('carousel_item_mob_1', 'carousel_item_mob_2', 'carousel_item_mob_3', 'carousel_item_mob_4', 'carousel_item_mob_5'),
		'closeup',
		('width', 'depth', 'height'),
		'product_inside', 
		'product_inside_pillow', 
		'carcas_type', 
		'paws_type', 
		'mechanism_type', 
		'sleep_place', 
		'linen_drawer', 
		'features',
		'pdf', 'scheme', 
		'options', 
		'slider_interior', 
		'popover', 
		('is_new', 'available_for_delivery_2','available_for_delivery_28', 'available_in_showroom'), 
		('show_on_category_page','popular'),
		'product_slug']
	save_on_top = True

	actions = ['duplicate_products']


	# Duplicate product
	def duplicate_products(self, request, queryset):
		for product in queryset:
			product.pk = None
			product.save()
		self.message_user(request, f"{len(queryset)} product(s) duplicated successfully.")
	duplicate_products.short_description = "Дублировать выбранные товары"


	# ADD photos preview in the list
	def get_html_img_preview(self, object):
		if object.product_img:
			return mark_safe(f'<img src="{object.product_img.url}" width=100>')
	get_html_img_preview.short_description = 'Превью'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_ru', 'category')
	prepopulated_fields = {"category_slug": ("category", )}

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
	list_display = ('collection',)
	prepopulated_fields = {"collection_slug": ("collection", )}


@admin.register(PopOverFeatures)
class PopOverFeaturesAdmin(admin.ModelAdmin):
	list_display = ('popover_name', 'popover_1_description', 'popover_2_description', 'popover_3_description', 'popover_4_description', 'popover_5_description')
	actions = ['duplicate_popovers']

	def duplicate_popovers(self, request, queryset):
		for popover in queryset:
			popover.pk = None
			popover.save()
		self.message_user(request, f"{len(queryset)} popover(s) duplicated successfully.")
	duplicate_popovers.short_description = "Дублировать набор 5-ти фич"


@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):
	list_display = ('fabric_name', 'get_html_fabric_preview', 'product_fabric_about', 'created', 'updated')
	fields = [
	'fabric_name',
	('product_fabric_img', 'get_html_fabric_preview'),
	'product_fabric_about'
	]
	readonly_fields = ('created', 'updated', 'get_html_fabric_preview')

	# ADD fabric preview in the list
	def get_html_fabric_preview(self, object):
		if object.product_fabric_img:
			return mark_safe(f'<img src="{object.product_fabric_img.url}" width=170>')
	get_html_fabric_preview.short_description = 'Миниатюра'



@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
	list_display = ('option_name', 'option_1_description', 'option_2_description', 'created', 'updated')

@admin.register(SliderInterior)
class SliderInteriorAdmin(admin.ModelAdmin):
	list_display = ('sl_interior_name', 'created', 'updated')


# class CustomProductForm(ProductForm):
# 	carousel_items = MultipleFileField(required=False)

# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		if self.instance.pk:
# 			self.fields['carousel_items'].initial = self.instance.carousel_items.all()

# 	def save(self, commit=True):
# 		product = super().save(commit=False)
# 		if commit:
# 			product.save()
# 		if self.cleaned_data.get('carousel_items'):
# 			for image in self.cleaned_data['carousel_items']:
# 				product.carousel_items.create(image=image)
# 		return product


# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ('image', 'product')
# admin.site.register(ProductImage, ProductImageAdmin)