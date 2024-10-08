from decimal import Decimal
from django.conf import settings
from product.models import Product
from django.shortcuts import get_object_or_404



class Cart:
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart


	def __iter__(self):
		product_slugs = self.cart.keys()
		products = [get_object_or_404(Product, product_slug=product_slug) for product_slug in product_slugs]
		cart = self.cart.copy()

		for product in products:
			cart[str(product.product_slug)]['product'] = product
		for item in cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item


	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())


	def add(self, product, quantity=1, override_quantity=False):
		product_slug = str(product.product_slug)
		if product_slug not in self.cart:
			self.cart[product_slug] = {'quantity': quantity, 'price': str(product.price)}
		else:
			if override_quantity:
				self.cart[product_slug]['quantity'] = quantity
			else:
				self.cart[product_slug]['quantity'] += quantity
		self.save()


	def save(self):
		self.session.modified = True


	def remove(self, product):
		product_slug = str(product.product_slug)
		if product_slug in self.cart:
			del self.cart[product_slug]
			self.save()

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity']
			for item in self.cart.values())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.save()