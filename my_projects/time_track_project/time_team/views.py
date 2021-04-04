from django.shortcuts import render,redirect

# Create your views here.
from .models import Team
from django.contrib.auth.decorators import login_required

#
#add view
@login_required
def add_team(request):
    template_name = 'team/add.html'
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            team = Team.objects.create(title=title,created_by=request.user)
            team.members.add(request.user)
            team.save()

            userProfile = request.user.UserProfile
            userProfile.active_team_id = team.id
            userProfile.save()
            return redirect('time-account')
    return render(request,template_name)

