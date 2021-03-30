from django.urls import path

from .views import time_frontpage,time_account,time_edit_profile

urlpatterns = [
    path('',time_frontpage,name='time-home'),
    path('time-account/',time_account,name='time-account'),
    path('edit/time-account/',time_edit_profile,name='time-edit-account'),
]
