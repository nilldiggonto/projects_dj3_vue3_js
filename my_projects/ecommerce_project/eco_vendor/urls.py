from django.urls import path
from .views import become_vendor,vendorView

urlpatterns = [
    path('',become_vendor,name='eco-become-vendor'),
    path('vendor-detail/',vendorView,name='eco-vendor-admin'),
]