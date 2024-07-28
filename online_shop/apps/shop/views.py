from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from ..cart.forms import CartAddProductForm


def index(request):
    return render(request, 'shop/index.html')


def product_list(request, category_id=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'form': cart_product_form
    }
    return render(request, 'shop/product_detail.html', context)
