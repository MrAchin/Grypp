# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/', views.cart_detail, name='cart_detail'),
]