from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView
from django.urls import reverse_lazy
# Create your views here.
class PasswordChangeView(PasswordChangeView):
    template_name = 'useres/password-change.html'
    success_url = reverse_lazy('users:password-reset')

class PasswordResetView(PasswordResetDoneView):
    template_name = 'useres/password-reset.html'
