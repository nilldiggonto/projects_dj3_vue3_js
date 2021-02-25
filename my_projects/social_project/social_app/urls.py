from django.urls import path
from .views import social_frontpage,signupView
from django.contrib.auth import views

urlpatterns = [
    path('',social_frontpage,name='social-home'),
    path('signup/',signupView,name='social-signup'),

    path('logout/',views.LogoutView.as_view(),name='social-logout'),
]