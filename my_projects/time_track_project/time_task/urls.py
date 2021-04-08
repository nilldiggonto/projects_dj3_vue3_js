from django.urls import path
from .views import time_projects

urlpatterns = [
    path('',time_projects,name='time-projects-list'),
]