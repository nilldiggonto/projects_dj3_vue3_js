from django.urls import path
from .views import become_vendor,vendorView,add_product,edit_vendor

urlpatterns = [
    path('',become_vendor,name='eco-become-vendor'),
    path('vendor-detail/',vendorView,name='eco-vendor-admin'),

    path('add-product/',add_product,name='eco-add-product'),
    path('edit-vendor/',edit_vendor,name='eco-edit-vendor'),
]