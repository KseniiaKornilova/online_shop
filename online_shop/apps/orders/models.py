from django.db import models
from ..shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя покупателя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия покупателя')
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    city = models.CharField(max_length=100, verbose_name='Город')
    paid = models.BooleanField(default=False, verbose_name='Оплачен ли заказ')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created']

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.orderitem_set.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    price = models.IntegerField(verbose_name='Цена товара')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество единиц товара')

    class Meta:
        verbose_name = 'Товар из заказа покупателя'
        verbose_name_plural = 'Товары из заказов покупателей'

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
