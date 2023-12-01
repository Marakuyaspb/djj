from django.contrib import admin
from .models import Post
from django.utils.translation import gettext_lazy as _

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'author', 'publish', 'status']
	list_filter = ['status', 'created', 'publish', 'author']
	search_fields = ['title', 'body']
	prepopulated_fields = {"slug": ("title",)}
	raw_id_fields = ['author']
	date_hierarchy = 'publish'
	ordering = ['status', 'publish']


	# def duplicate_event(ModelAdmin, request, queryset):
	# 	for object in queryset:
	# 		object.id = None
	# 		object.save()
	# 	duplicate_event.short_description = "Duplica Record Selezionati"