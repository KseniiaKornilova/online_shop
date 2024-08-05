from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from ..orders.models import Order


@shared_task
def payment_completed(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Чек оплаты'
    message = 'Здравствуйте! Ниже прикреплен pdf-файл с чеком для Вашего заказа'
    email = EmailMessage(subject, message, 'ksyu_kornilova@mail.ru', [order.email])

    html = render_to_string('orders/pdf.html', {'order': order})
    out = BytesIO()
    weasyprint.HTML(string=html).write_pdf(out)

    email.attach(f'заказ_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')
    email.send()
