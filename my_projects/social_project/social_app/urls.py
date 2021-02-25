from django.urls import path
from .views import social_frontpage

urlpatterns = [
    path('',social_frontpage,name='social-home'),
]