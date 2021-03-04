from django.urls import path
from .views import notificationsView

urlpatterns = [
    path('',notificationsView,name='social-notification'),
]