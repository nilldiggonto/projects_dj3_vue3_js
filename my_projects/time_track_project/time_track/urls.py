from django.urls import path

from .views import time_frontpage

urlpatterns = [
    path('',time_frontpage,name='time-home'),
]
