from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset()\
			.filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

	class Status(models.TextChoices):
		DRAFT = 'DF', 'Draft'
		PUBLISHED = 'PB', 'Published'

	title = models.CharField(max_length=250, verbose_name = 'Заголовок')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	author = models.ForeignKey(User,
		on_delete=models.CASCADE,
		related_name='blog_posts', verbose_name = 'Автор')
	body = models.TextField(verbose_name = 'Текст поста')
	publish = models.DateTimeField(default=timezone.now, verbose_name = 'Опубликовано')
	created = models.DateTimeField(auto_now_add=True, verbose_name = 'Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name = 'Обновлено')
	status = models.CharField(max_length=2,
		choices=Status.choices,
		default=Status.DRAFT, verbose_name = 'Статус')

	objects = models.Manager() # default
	published = PublishedManager() # show published
	#tags = TaggableManager()

	class Meta:
		ordering = ['-publish']
		indexes = [
		models.Index(fields=['-publish']),
		]
		verbose_name = 'Запись в блоге'
		verbose_name_plural = 'Записи в блоге'

	def __str__(self):
		return self.title


