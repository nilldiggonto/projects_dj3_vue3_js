from django.urls import path

from .views import time_frontpage,time_account

urlpatterns = [
    path('',time_frontpage,name='time-home'),
    path('time-account/',time_account,name='time-account'),
]
