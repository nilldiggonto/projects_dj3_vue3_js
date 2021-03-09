from django.urls import path
from .views import productDetail

urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/',productDetail,name='eco-p-detail'),
]