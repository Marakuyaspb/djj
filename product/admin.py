from .models import Category, Collection, Fabric, Product, ProductImage
from django.contrib import admin


admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Fabric)


# class ProductCarouselInline(admin.TabularInline):
#     model = Product.carousel_items.through
#     extra = 1

# class ProductCarouselMobImageInline(admin.TabularInline):
#     model = Product.carousel_items_mob.through
#     extra = 1

# class ProductInteriorImageInline(admin.TabularInline):
#     model = Product.slider_interior.through
#     extra = 1

# class ProductInteriorMobImageInline(admin.TabularInline):
#     model = Product.slider_interior_mob.through
#     extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['product_full_name', 'fabric_name', 'is_new', 'available_for_delivery_2', 'available_for_delivery_28', 'available_in_showroom', 'created', 'updated']
	search_fields = ['collection', 'category', 'category_ru', 'product_full_name', 'fabric_name']
	prepopulated_fields = {
	'slug': ('collection','category','fabric_name'),
	}
	# inlines = [ProductCarouselInline, ProductCarouselMobImageInline, ProductInteriorImageInline, ProductInteriorMobImageInline],


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
	model = ProductImage
	list_display = ['image']