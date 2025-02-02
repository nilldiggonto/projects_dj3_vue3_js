from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProjectTask,TaskPrimary,Entry
from datetime import datetime
# import datetime

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
            messages.info(request,'Project Created')

            return redirect('time-projects-list')
    

    return render(request,template_name,{'team':team,'projects':projects})
    

@login_required
def time_projectDetail(request,project_id):
    team = get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE)
    project = get_object_or_404(ProjectTask,team=team,pk=project_id)

    template_name = 'project/project_detail.html'

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task = TaskPrimary.objects.create(team=team,project=project,title=title,created_by=request.user)
            messages.info(request,'Task Created')
            return redirect('time-project-detail', project_id=project.id)

    tasks_todo = project.tasks.filter(status=TaskPrimary.TODO)
    tasks_done = project.tasks.filter(status=TaskPrimary.DONE)
    context = {
        'team':team,
        'project':project,
        'tasks_todo':tasks_todo,
        'tasks_done':tasks_done
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
            messages.info(request,'Project updated')
            return redirect('time-project-detail', project_id=project.id)
    context = {
        'team':team,
        'project':project
    }
    return render(request,template_name,context)


@login_required
def task_detail(request,project_id,task_id):
    team = get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE)
    project = get_object_or_404(ProjectTask,team=team,pk=project_id)
    task = get_object_or_404(TaskPrimary,pk=task_id,team=team)
    # tempalte_nam
    template_name='project/task_detail.html'

    if request.method == 'POST':
        hours = int(request.POST.get('hours',0))
        minutes = int(request.POST.get('minutes',0))
        date = '%s %s' % (request.POST.get('date'), datetime.now().time())
        minutes_total = (hours*60) + minutes
        entry = Entry.objects.create(team=team,project=project,task=task,minutes=minutes_total,created_by = request.user, created_at =date,is_track=True)
        messages.info(request,'Time Added')
    context = {
        'team':team,
        'project':project,
        'task':task,
        'today':datetime.today()
        # 'tasks_todo':tasks_todo,
        # 'tasks_done':tasks_done
    }


    return render(request,template_name,context)


@login_required
def task_edit(request,project_id,task_id):
    team = get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE)
    project = get_object_or_404(ProjectTask,team=team,pk=project_id)
    task = get_object_or_404(TaskPrimary,pk=task_id,team=team)
    # tempalte_nam
    template_name='project/task_edit.html'

    if request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')

        if title:
            task.title = title
            task.status = status
            task.save()
            messages.info(request,'Task Updated')
            return redirect('time-task-detail',project_id = project.id, task_id= task.id)

    context = {
        'team':team,
        'project':project,
        'task':task
        # 'tasks_todo':tasks_todo,
        # 'tasks_done':tasks_done
    }

    


    return render(request,template_name,context)


#edit entry
@login_required
def edit_entry(request,project_id,task_id,entry_id):
    team = get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE)
    project = get_object_or_404(ProjectTask,team=team,pk=project_id)
    task = get_object_or_404(TaskPrimary,pk=task_id,team=team)
    entry = get_object_or_404(Entry,pk=entry_id,team=team)

    if request.method == 'POST':
        hours = int(request.POST.get('hours',0))
        minutes = int(request.POST.get('minutes',0))
        date = '%s %s' % (request.POST.get('date'), datetime.now().time())

        entry.created_at = date
        entry.minutes = (hours*60) + minutes
        entry.save()
        messages.info(request,'Activity updated')
        return redirect('time-task-detail',project_id = project.id, task_id= task.id)

    hours,minutes = divmod(entry.minutes,60)
    template_name = 'project/entry_edit.html'
    context = {
        'team':team,
        'project':project,
        'task':task,
        'entry':entry,
        'hours':hours,
        'minutes':minutes
        # 'tasks_todo':tasks_todo,
        # 'tasks_done':tasks_done
    }

    return render(request,template_name,context)


#delete entry
@login_required
def delete_entry(request,project_id,task_id,entry_id):
    team = get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE)
    project = get_object_or_404(ProjectTask,team=team,pk=project_id)
    task = get_object_or_404(TaskPrimary,pk=task_id,team=team)
    entry = get_object_or_404(Entry,pk=entry_id,team=team)
    entry.delete()

    messages.info(request,'Activity Deleted')
    
    return redirect('time-task-detail',project_id = project.id, task_id= task.id)




    


