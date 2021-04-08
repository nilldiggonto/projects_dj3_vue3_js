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

    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)

        if title:
            project = ProjectTask.objects.create(team=team,title=title,created_by=request.user)

            return redirect('time-projects-list')

    return render(request,template_name,{'team':team,'projects':projects})
    

@login_required
def time_projectDetail(request,project_id):
    team = get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE)
    project = get_object_or_404(ProjectTask,team=team,pk=project_id)

    template_name = 'project/project_detail.html'
    context = {
        'team':team,
        'project':project
    }
    return render(request,template_name,context)