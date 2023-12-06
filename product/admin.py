from django.contrib import admin
from .forms import CustomProductForm
from .models import Category, Collection, Option, Fabric, Product, ProductImage, PopOverFeatures
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.forms import CheckboxSelectMultiple



class ProductCarouselInline(admin.TabularInline):
	model = Product.carousel_items.through
	extra = 1

class ProductCarouselMobInline(admin.TabularInline):
	model = Product.carousel_items_mob.through
	extra = 1

class ProductInteriorInline(admin.TabularInline):
	model = Product.interior_items.through
	extra = 1

class ProductInteriorMobInline(admin.TabularInline):
	model = Product.interior_items_mob.through
	extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('product_full_name', 'fabric_name', 'price', 'price_sale', 'show_on_category_page', 'popular', 'is_new', 'available_in_showroom', 'available_for_delivery_2', 'created', 'updated')
	form = CustomProductForm
	#inlines = [ProductCarouselInline, ProductCarouselMobInline, ProductInteriorInline, ProductInteriorMobInline]
	actions = ['duplicate_products']

	def duplicate_products(self, request, queryset):
		for product in queryset:
			product.pk = None
			product.save()
		self.message_user(request, f"{len(queryset)} product(s) duplicated successfully.")
	duplicate_products.short_description = "Дублировать выбранные товары"



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
	list_display = ('fabric_name', 'product_fabric_about', 'created', 'updated')
@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
	list_display = ('option_name', 'option_1_description', 'option_2_description', 'created', 'updated')



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