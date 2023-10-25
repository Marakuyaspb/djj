from django.db import models
from django.conf import settings

def images_path():
    return os.path.join(settings.MEDIA_ROOT, "img")

class ItemCard(models.Model):
	collection = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	category_ru = models.CharField(max_length=50)
	product_name = models.CharField(max_length=50)
	product_full_name  = models.CharField(max_length=80)
	product_img = models.FilePathField(path=images_path)
	description = models.CharField(max_length=1500)
	price = models.IntegerField(blank=True, null=True)
	price_sale = models.IntegerField(blank=True, null=True)
	is_new = models.FilePathField(path=images_path)
	# is_new = models.BooleanField(default=False)
	available_for_delivery_2 = models.FilePathField(path=images_path)
	available_for_delivery_28 = models.FilePathField(path=images_path)
	available_in_showroom = models.FilePathField(path=images_path)
	fabric_type = models.CharField(max_length=50)
	fabric_name = models.CharField(max_length=50)
	product_fabric_about = models.CharField(max_length=700)
	product_fabric_img = models.FilePathField(path=images_path)
	carousel_item = models.FilePathField(path=images_path)
	carousel_item_mob = models.FilePathField(path=images_path)
	closeup = models.FilePathField(path=images_path)
	slider_interior = models.FilePathField(path=images_path)
	slider_interior_mob = models.FilePathField(path=images_path)	
	prod_width = models.IntegerField(blank=True, null=True)
	prod_depth = models.IntegerField(blank=True, null=True)
	prod_height = models.IntegerField(blank=True, null=True)
	scheme = models.FilePathField(path=images_path)
	slug = models.SlugField(max_length=250)

	def __str__(self):
		return self.product_name