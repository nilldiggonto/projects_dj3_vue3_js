from django.urls import path
from .views import conversationView,conversationRecipient
from .api import api_add_message

urlpatterns = [
    path('',conversationView,name='social-converse'),
    path('chat/<int:user_id>/',conversationRecipient,name='social-converse-one'),

    path('api/add_message/',api_add_message,name='social-add-message'),
]