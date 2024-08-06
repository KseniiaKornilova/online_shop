from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from ..cart.cart import Cart
from ..shop.recommender import Recommender


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()   # создание заказа в БД
            products = []
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
                products.append(item['product'])
            cart.clear()

            r = Recommender()
            r.products_bought(products)

            order_created.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
        return render(request, 'orders/create_order.html', {'cart': cart, 'form': form})
