from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
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

            userProfile = request.user.timeprofile
            userProfile.active_team_id = team.id
            userProfile.save()
            return redirect('time-account')
    return render(request,template_name)

@login_required
def team(request,team_id):
    team = get_object_or_404(Team,pk=team_id,status=Team.ACTIVE,members__in=[request.user])
    tempalte_name ='team/team.html'
    return render(request,'team/team.html',{'team':team})

@login_required
def edit_team(request):
    team = get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE,members__in=[request.user])
    # team = get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE,)
    template_name = 'team/edit.html'
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            team.title = title
            team.save()
            messages.info(request,'Saved changes')
            return redirect('time-team-details', team_id=team.id)
    return render(request,template_name,{'team':team})

