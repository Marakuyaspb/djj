from django.db import models
from product.models import Product

class Order(models.Model):
	first_name = models.CharField(max_length=60, verbose_name = 'Ваше имя')
	city = models.CharField(max_length=100, verbose_name = 'Город')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	email = models.EmailField(verbose_name = 'E-mail')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['-created']
		indexes = [
		models.Index(fields=['-created']),
		]
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

	def __str__(self):
		return f'Order {self.id}'

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)
	
	def __str__(self):
		return str(self.id)
		
	def get_cost(self):
		return self.price * self.quantity