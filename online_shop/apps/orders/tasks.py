from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Ваш заказ №{order_id}'
    html_message = render_to_string('orders/send_mail.html', {'order': order})
    text_message = strip_tags(html_message)
    email = EmailMultiAlternatives(subject, text_message, 'ksyu_kornilova@mail.ru', [order.email])
    email.attach_alternative(html_message, 'text/html')
    email.send()
