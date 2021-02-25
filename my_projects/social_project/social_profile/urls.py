from django.urls import path
from .views import socialprofileView

urlpatterns = [
    path('<str:username>',socialprofileView,name='social-profile'),
]