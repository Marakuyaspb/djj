from django.contrib import admin
from .models import Category, Collection, Option, Fabric, Product, SliderInterior,PopOverFeatures
# from .forms import ProductForm, FabricIconForm, OptionForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.forms import CheckboxSelectMultiple




class FabricAdmin(admin.ModelAdmin):
	list_display = ('fabric_name', 'product_fabric_about', 'created', 'updated')

class OptionAdmin(admin.ModelAdmin):
	list_display = ('option_name', 'option_1_description', 'option_2_description', 'created', 'updated')

# class ProductImageAdmin(admin.StackedInline):
# 	model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('product_full_name', 'fabric_name', 'price', 'price_sale', 'show_on_category_page', 'popular', 'is_new', 'available_in_showroom', 'available_for_delivery_2', 'created', 'updated')
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
class CategoryAdmin(admin.ModelAdmin):
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


admin.site.register(Fabric, FabricAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(SliderInterior)





# class ForModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.ManyToManyField: {'widget': CheckboxSelectMultiple},
#     }

# admin.site.register(ForModelAdmin)


# class FabricIconChangeInline(admin.TabularInline):
#     model = FabricIconChange
# class FabricIconChangeAdmin(FabricIconChange):
#     form = FabricIconForm

# admin.site.register(FabricIconChange, FabricIconChangeAdmin)


# @admin.register(Option)
# class OptionAdminInline(admin.TabularInline):
#     model = FabricIconChange
# class OptionAdmin(Option):
#     form = OptionForm

# admin.site.register(Option, OptionAdmin)


# @admin.register(Product)
# class ProductOptionInline(admin.TabularInline):
#     model = ProductOption


# class ProductAdmin(Product):
# 	form = ProductForm
# 	inlines = [ProductOptionInline, FabricIconChangeInline]
	
# 	def display_options(self, obj):
# 		return ', '.join([str(option.option_name)
#         	for option in obj.options.all()])
# 	display_options.short_description = 'Options'

# 	def display_fabric_icons(self, obj):
# 		return ', '.join([str(icon.product_fabric_icon.url)
# 			for icon in obj.product_fabric_icon.all()])
# 	display_fabric_icons.short_description = 'Fabric Icons'

# 	list_display = ['product_full_name', 'display_fabric_icons', 'display_options', 'price', 'is_new', 'available_for_delivery_2', 'available_for_delivery_28', 'available_in_showroom', 'created', 'updated']
# 	list_filter = ['popular']
# 	filter_horizontal = ('options',)
# 	prepopulated_fields = {'slug': ('collection', 'category', 'fabric_name')}
# 	search_fields = ['collection', 'category', 'category_ru', 'product_full_name', 'fabric_name']
# 	fieldsets = [
#         (None, {
#             'fields': ('product_full_name', 'product_type', 'product_img', 'popular', 'is_new', 'available_for_delivery_2', 'available_for_delivery_28', 'available_in_showroom','description', 'price', 'price_sale', 'width', 'depth', 'height', 'pdf', 'product_inside', 'product_inside_pillow', 'carcas_type', 'paws_type', 'mechanism_type', 'sleep_place', 'linen_drawer', 'scheme', 'features')
#         })
#     ]


# admin.site.register(ProductAdmin, ProductOptionInline)

