from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from product.models import Product
from .cart import Cart
from .forms import CartAddProductForm



@require_POST
def cart_add(request, product_slug):
	cart = Cart(request)
	product = get_object_or_404(Product, product_slug=product_slug)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
	return redirect('cart:cart_detail')



@require_POST
def cart_remove(request, product_slug):
	cart = Cart(request)
	product = get_object_or_404(Product, product_slug=product_slug)
	cart.remove(product)
	return redirect('cart:cart_detail')



def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
	return render(request, 'cart/detail.html', {'cart': cart})

#EXPERIMENTS
# def cart_detail(request):
# 	cart = Cart(request)
# 	items = []
	
# 	for item in cart:
# 		product = item['product']
# 		update_quantity_form = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
# 		items.append({'product': product, 'quantity': item['quantity'], 'update_quantity_form': update_quantity_form})

# 	return render(request, 'cart/detail.html', {'items': items, 'total_price': cart.get_total_price()})