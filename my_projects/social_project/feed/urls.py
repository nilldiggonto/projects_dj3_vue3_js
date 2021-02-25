from django.urls import path
from .views import feedView

urlpatterns = [
    path('',feedView,name='social-feed'),
]