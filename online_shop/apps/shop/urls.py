from django.urls import path
from . import views


app_name = 'shop'


urlpatterns = [
    path('', views.index, name='main_page'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_list/<int:category_id>/', views.product_list, name='product_list_by_category'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
]
