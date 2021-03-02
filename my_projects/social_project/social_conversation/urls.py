from django.urls import path
from .views import conversationView

urlpatterns = [
    path('',conversationView,name='social-converse'),
]