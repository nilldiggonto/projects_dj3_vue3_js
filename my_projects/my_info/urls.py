from .views import my_home
from django.urls import path

urlpatterns = [
    path('',my_home,name='my-home'),
]