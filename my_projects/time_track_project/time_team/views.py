from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
# Create your views here.
from .models import Team,Invitation
from django.contrib.auth.decorators import login_required

import random

from .utils import send_invitation,send_invitation_accepted
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


@login_required
def activate_team(request,team_id):
    team = get_object_or_404(Team,pk=team_id,status=Team.ACTIVE,members__in=[request.user])
    timeprofile = request.user.timeprofile
    timeprofile.active_team_id = team.id
    timeprofile.save()
    messages.info(request,'Team Activated')
    return redirect('time-account')



@login_required
def inviteView(request):
    team = get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE)

    if request.method == 'POST':
        email =  request.POST.get('email')

        if email:
            invitations = Invitation.objects.filter(team=team,email=email)

            if not invitations:
                code = ''.join(random.choice('abcdefghijklmnopqrstuves123456789') for i in range(4))
                invitation = Invitation.objects.create(team=team,email=email,code=code)

                messages.info(request,'The user has invitation')

                send_invitation(email,code,team)

                return redirect('time-team-details',team_id=team.id)
            else:
                messages.info(request,'Invitation already send')
    return render(request,'team/invite.html',{'team':team})
    
