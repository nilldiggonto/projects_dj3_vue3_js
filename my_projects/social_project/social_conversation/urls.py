from django.urls import path
from .views import conversationView,conversationRecipient

urlpatterns = [
    path('',conversationView,name='social-converse'),
    path('chat/<int:user_id>/',conversationRecipient,name='social-converse-one'),
]