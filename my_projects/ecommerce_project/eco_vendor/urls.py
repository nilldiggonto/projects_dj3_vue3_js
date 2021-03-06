from django.urls import path
from .views import become_vendor

urlpatterns = [
    path('',become_vendor,name='eco-become-vendor'),
]