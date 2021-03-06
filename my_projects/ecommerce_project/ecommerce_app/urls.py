from django.urls import path
from .views import ecoView

urlpatterns = [
    path('',ecoView,name='eco-home'),
]