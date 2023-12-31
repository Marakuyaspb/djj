from .models import OrderItem, Order
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart
import os

from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.core.mail import send_mail, send_mass_mail
from django.template import loader


#ПРОСТО ЗАКАЗ

def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(order=order, product=item['product'],	price=item['price'], quantity=item['quantity'])
			cart.clear()


		# отправить письмо покупателю
			# subject = f'DECONA. Заказ № {order.id}'
			# message = f'Здавствуйте, {order.first_name}!\n Ваш заказ успешно оформлен, скоро с вами свяжется наш менеджер.\n Данные заказа:\n Ваш № заказа: {order.id}\n Имя: {order.first_name} | Город: {order.city}.\n E-mail: {order.email}\n Телефон: {order.phone}'

			# send_mail(subject, message, settings.EMAIL_HOST_USER, [order.email])


			# МАНАГЕРАМ ПИСЬМО
			context = {
			  'order': order,
			}
			send_mail('Новый заказ', 
				'Здавствуйте, {order.first_name}!', 
				settings.EMAIL_HOST_USER,
				['komy.kabachok@yandex.ru'],
  			fail_silently=True,
  			html_message=loader.get_template('orders/order/email.html').render(context)
  		)




			return render(request, 'orders/order/created.html', {'order': order})
	else:
		form = OrderCreateForm()
	return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})




@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	html = render_to_string('orders/order/pdf.html', {'order': order})
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
	stylesheet_path = os.path.join(settings.STATIC_ROOT, 'css/pdf.css')
	weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(filename=stylesheet_path)])
	return response






# ЗАКАЗ И ОПЛАТА

# def order_create(request):
# 	cart = Cart(request)
# 	if request.method == 'POST':
# 		form = OrderCreateForm(request.POST)
# 		if form.is_valid():
# 			order = form.save()
# 			for item in cart:
# 				OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
# 			cart.clear()
# 			order_created.delay(order.id)
# 			request.session['order_id'] = order.id
# 	# перенаправить к платежу
# 			return redirect(reverse('payment:process'))
# 	else:
# 		form = OrderCreateForm()
# 	return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


# @staff_member_required
# def admin_order_detail(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     return render(request,
#                   'admin/orders/order/detail.html',
#                   {'order': order})

# @staff_member_required
# def admin_order_pdf(request, order_id):
# 	order = get_object_or_404(Order, id=order_id)
# 	html = render_to_string('orders/order/pdf.html', {'order': order})
# 	response = HttpResponse(content_type='application/pdf')
# 	response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
# 	stylesheet_path = os.path.join(settings.STATIC_ROOT, 'css/pdf.css')
# 	weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(filename=stylesheet_path)])
# 	return response