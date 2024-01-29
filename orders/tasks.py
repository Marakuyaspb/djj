from io import BytesIO
from django.conf import settings
from celery import shared_task
#import weasyprint
#from weasyprint import HTML
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import Order


@shared_task
def order_created(order_id):
  order = Order.objects.get(id=order_id)
  subject = f'Новый заказ № {order.id}'
  message = f'Уважаемый {order.first_name}!\n\n' \
    f'Ваш заказ успешно оформлен, скоро с вами свяжется наш менеджер.' \
    f'Номер вашего заказа: {order.id}.'
  email = EmailMessage(subject, message, 'settings.EMAIL_HOST_USER', [order.email])

  html = render_to_string('orders/order/email.html', {'order': order})
  email.attach_alternative(html, "text/html")
  out = BytesIO()
  stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
  weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
  email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
  email.send()

 # Send email to admin
  admin_subject = f'New order № {order.id}'
  admin_message = f'New order received with order number: {order.id}.'
  admin_email = EmailMessage(admin_subject, admin_message, settings.EMAIL_HOST_USER, ['admin@example.com'])
  admin_email.send()