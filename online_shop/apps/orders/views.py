from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from ..cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()   # создание заказа в БД
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderCreateForm()
        return render(request, 'orders/create_order.html', {'cart': cart, 'form': form})
