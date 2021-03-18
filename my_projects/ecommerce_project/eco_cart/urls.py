from django.urls import path
from .views import cart_detail,order_success

urlpatterns = [
    path('',cart_detail,name='eco-cart'),
    path('success/',order_success,name='eco-cart-success'),
]