from .views import PasswordChangeView,PasswordResetView
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('change-password/',PasswordChangeView.as_view(),name='passsword-change'),
    path('reset-password/',PasswordResetView.as_view(),name='password-reset'),
]