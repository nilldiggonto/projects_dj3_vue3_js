from django.urls import path,include
from .views import ecoView

urlpatterns = [
    path('',ecoView,name='eco-home'),
    path('-be/vendor/',include('ecommerce_project.eco_vendor.urls')),
]