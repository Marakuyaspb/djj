from celery import shared_task
from django.core.mail import send_mail, send_mass_mail
from .models import Order


@shared_task
def order_created(order_id):
  Order.objects.get(id=order_id)
  message_to_client = (
    'Заказ № {order.id}',
    'Здравствуйте, {order.first_name}! Ваш заказ успешно оформлен, скоро с вами свяжется наш менеджер. Номер вашего заказа: {order.id}.',
    settings.EMAIL_HOST_USER,
    '[order.email]'
  )

  message_to_mannager = (
    'Новый заказ № {order.id}',
    'Номер заказа: {order.id}.\n Данные покупателя: \n Имя: {order.first_name} \n Город: {order.city} \n Телефон: {order.phone} \n Почта: {order.email}',
    settings.EMAIL_HOST_USER,
    'hto.order@gmail.com'
  )


  send_mass_mail((message_to_client, message_to_mannager), fail_silently=False)
