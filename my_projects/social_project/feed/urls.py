from django.urls import path
from .views import feedView,searchView
from .api import api_add_feed

urlpatterns = [
    path('',feedView,name='social-feed'),
    path('search/',searchView,name='social-search'),

    #api
    path('api/add_social/',api_add_feed,name='social-add-api'),
]