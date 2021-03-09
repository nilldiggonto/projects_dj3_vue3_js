from django.urls import path
from .views import productDetail,category

urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/',productDetail,name='eco-p-detail'),
    path('<slug:category_slug>/',category,name='eco-category'),
]