from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from time_track_project.time_profile.models import UserProfile
from time_track_project.time_team.models import Invitation

# Create your views here.
def social_frontpage(request):
    template_name = 'social_app/social.html'
    return render(request,template_name)


## SIGNUP VIEW
def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()
            userprofile = UserProfile.objects.create(user=user)
            login(request,user)

            invitations = Invitation.objects.filter(email=user.email,status=Invitation.INVITED)
            if invitations:
                return redirect('time-accept-invite')
            else:
                return redirect('time-dashboard')

            return redirect('homepage')
    else:
        form = UserCreationForm()
    template_name = 'social_app/signup.html'
    return render(request,template_name,{'form':form})
    # context = {
    #     'form':form,
    # }