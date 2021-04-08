from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProjectTask

from time_track_project.time_team.models import Team
# Create your views here.

#list projects
@login_required
def time_projects(request):
    template_name = 'project/projects.html'
    team = get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE)
    projects = team.projects.all()

    return render(request,template_name,{'team':team,'projects':projects})
