from django.contrib import admin
from .models import Category, Collection, Option, Fabric, FabricIconChange, Product
# from .forms import ProductForm, FabricIconForm, OptionForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.forms import CheckboxSelectMultiple


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

# 	# def duplicate_event(ProductAdmin, request, queryset):
# 	# 	for object in queryset:
# 	# 		object.id = None
# 	# 		object.save()
# 	# 	duplicate_event.short_description = "Duplica Record Selezionati"

# admin.site.register(ProductAdmin, ProductOptionInline)



admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Fabric)
admin.site.register(Option)
admin.site.register(FabricIconChange)
admin.site.register(Product)