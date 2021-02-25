from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
# Create your views here.
def socialprofileView(request,username):
    user = get_object_or_404(User,username=username)

    context = {
        'user':user,
    }
    template_name = 'social_profile/social_profile.html'

    return render(request,template_name,context)
