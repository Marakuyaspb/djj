from django import forms
from .models import Category, Collection, Fabric, Option, Product
from .forms import ProductForm
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Fabric)
admin.site.register(Option)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	# model = Product
	form = ProductForm
	list_display = ['product_full_name', 'price', 'is_new', 'available_for_delivery_2', 'available_for_delivery_28', 'available_in_showroom', 'created', 'updated']
	list_filter = ['popular']
	search_fields = ['collection', 'category', 'category_ru', 'product_full_name', 'fabric_name']
	fieldsets = [
        (None, {
            'fields': ('product_full_name', 'product_type', 'product_img', 'popular', 'is_new', 'available_for_delivery_2', 'available_for_delivery_28', 'available_in_showroom', 'fabric_current','description', 'price', 'price_sale', 'carousel_items', 'carousel_items_mob', 'closeup', 'slider_interior', 'slider_interior_mob', 'width', 'depth', 'height', 'pdf', 'product_inside', 'product_inside_pillow', 'carcas_type', 'paws_type', 'mechanism_type', 'sleep_place', 'linen_drawer', 'scheme', 'option', 'features')
        })
    ]

	def duplicate_event(ProductAdmin, request, queryset):
		for object in queryset:
			object.id = None
			object.save()
		duplicate_event.short_description = "Duplica Record Selezionati"





	def fabric_icon(self, obj):
		pass
        # return '<img src="%s" width="50" />' % obj.fabric.product_fabric_icon.url

    # fabric_icon.allow_tags = True
    # fabric_icon.short_description = 'Fabric Icon'



class ProductForm(forms.ModelForm):
    fabric_1 = forms.ModelChoiceField(queryset=Fabric.objects.all())
    fabric_2 = forms.ModelChoiceField(queryset=Fabric.objects.all())
    fabric_3 = forms.ModelChoiceField(queryset=Fabric.objects.all())
    fabric_4 = forms.ModelChoiceField(queryset=Fabric.objects.all())
    fabric_5 = forms.ModelChoiceField(queryset=Fabric.objects.all())

    class Meta:
        model = Product
        exclude = ('fabrics',)

# class ProductAdmin(admin.ModelAdmin):
#     form = ProductForm



	# prepopulated_fields = {
	# 'slug': ('collection','category','fabric_name'),
	# }


	# inlines = [ProductCarouselInline, ProductCarouselMobImageInline, ProductInteriorImageInline, ProductInteriorMobImageInline],


# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
# 	model = ProductImage
# 	list_display = ['image']