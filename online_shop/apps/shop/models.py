from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория товаров')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория товара')
    name = models.CharField(max_length=200, verbose_name='Название товара')
    image = models.ImageField(upload_to='products', blank=True, verbose_name='Изображение товара')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.IntegerField(verbose_name='Стоимость товара')
    available = models.BooleanField(default=True, verbose_name='В наличии ли товар')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания объявления')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления объявления')

    def __str__(self):
        return f'{self.category} : {self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']
