from django.urls import path,include
from .views import social_frontpage,signupView
from django.contrib.auth import views

urlpatterns = [
    path('',social_frontpage,name='social-home'),
    path('signup/',signupView,name='social-signup'),
    path('login/',views.LoginView.as_view(template_name='social_app/login.html'),name='social-login'),

    path('logout/',views.LogoutView.as_view(),name='social-logout'),

    path('-feed/',include('social_project.feed.urls')),
    path('-social-profile/',include('social_project.social_profile.urls')),
    path('-converse/',include('social_project.social_conversation.urls')),
    path('-notification/',include('social_project.social_notification.urls')),
]