from django.urls import path
from .views import social_frontpage,signupView

urlpatterns = [
    path('',social_frontpage,name='social-home'),
    path('signup/',signupView,name='social-signup'),
]