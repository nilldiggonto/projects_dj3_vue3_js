from django.urls import path
from .views import timeDashboard
urlpatterns = [
    path('',timeDashboard,name='time-dashboard'),

]