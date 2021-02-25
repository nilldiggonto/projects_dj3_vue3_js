from django.urls import path
from .views import feedView
from .api import api_add_feed

urlpatterns = [
    path('',feedView,name='social-feed'),

    #api
    path('api/add_social/',api_add_feed,name='social-add-api'),
]