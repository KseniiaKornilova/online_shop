from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'last_name']
    search_fields = ('last_name',)
    inlines = [OrderItemInline]
