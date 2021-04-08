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
            messages.info(request,'Task Created')

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


#eidt
@login_required
def time_projectEdit(request,project_id):
    team = get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE)
    project = get_object_or_404(ProjectTask,team=team,pk=project_id)

    template_name = 'project/project_edit.html'

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            project.title= title
            project.save()
            messages.info(request,'Task updated')
            return redirect('time-project-detail', project_id=project.id)
    context = {
        'team':team,
        'project':project
    }
    return render(request,template_name,context)
    


