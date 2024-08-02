from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Ваш заказ №{order_id}'
    message = f'Здравствуйте, {order.first_name}, \n' \
              f'Ваш заказ был успешно оформлен! Номер заказа: {order_id}'
    mail_sent = send_mail(subject, message, 'ksyu_kornilova@mail.ru', [order.email])
    return mail_sent
