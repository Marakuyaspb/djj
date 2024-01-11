from io import BytesIO
from django.conf import settings
from celery import shared_task
#import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
#from django.core.mail import send_mail, send_mass_mail
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







# @shared_task
# def order_created(order_id):
#   order = Order.objects.get(id=order_id)
#   subject = f'Новый заказ № {order.id}'
#   message = f'Уважаемый {order.first_name}!\n\n' \
#     f'Ваш заказ успешно оформлен, скоро с вами свяжется наш менеджер.' \
#     f'Номер вашего заказа: {order.id}.'
#   mail_sent = send_mail(subject,
#     message,
#     'settings.EMAIL_HOST_USER',
#     [order.email])
#   return mail_sent



# @shared_task
# def order_created(order_id):
#   Order.objects.get(id=order_id)
#   message_to_client = (
#     'Заказ № {order.id}',
#     'Здравствуйте, {order.first_name}! Ваш заказ успешно оформлен, скоро с вами свяжется наш менеджер. Номер вашего заказа: {order.id}.',
#     settings.EMAIL_HOST_USER,
#     '[order.email]'
#   )

#   message_to_mannager = (
#     'Новый заказ № {order.id}',
#     'Номер заказа: {order.id}.\n Данные покупателя: \n Имя: {order.first_name} \n Город: {order.city} \n Телефон: {order.phone} \n Почта: {order.email}',
#     settings.EMAIL_HOST_USER,
#     'hto.order@gmail.com'
#   )


#   send_mass_mail((message_to_client, message_to_mannager), fail_silently=False)