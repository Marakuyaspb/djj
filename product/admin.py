from django.contrib import admin
from .models import Category, Collection, Product

admin.site.register(Category)

admin.site.register(Collection)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['product_full_name', 'fabric_name', 'is_new', 'available_for_delivery_2', 'available_for_delivery_28', 'available_in_showroom', 'created', 'updated']
	search_fields = ['collection', 'category', 'category_ru', 'product_full_name', 'fabric_name']
	prepopulated_fields = {'slug': ('collection','category','fabric_name')}
