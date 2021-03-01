from django import forms
from .models import SocialProfile

class SocialProfileForm(forms.ModelForm):
    class Meta:
        model = SocialProfile
        fields = ('avatar',)