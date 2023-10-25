from django.contrib import admin
from .models import Category, Collection, Product

admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Product)