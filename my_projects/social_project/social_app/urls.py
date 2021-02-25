from django.urls import path
from .views import social_frontpage,signupView
from django.contrib.auth import views

urlpatterns = [
    path('',social_frontpage,name='social-home'),
    path('signup/',signupView,name='social-signup'),
    path('login/',views.LoginView.as_view(template_name='social_app/login.html'),name='social-login'),

    path('logout/',views.LogoutView.as_view(),name='social-logout'),
]