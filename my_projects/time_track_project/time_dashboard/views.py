from django.shortcuts import render,redirect,get_object_or_404
from datetime import datetime,timedelta,timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from dateutil.relativedelta import relativedelta

from time_track_project.time_task.models import ProjectTask,Entry
from time_track_project.time_team.models import Team

from .utils import (get_time_for_user_and_date,get_time_for_team_and_month,
                    get_time_for_uer_and_month,get_time_for_user_and_project_and_month,
                    get_time_for_user_and_team_month)

# Create your views here.

@login_required
def timeDashboard(request):
    template_name = 'time_dashboard/dashboard.html'

    if not request.user.timeprofile.active_team_id:
        return redirect('time-account')

    team = get_object_or_404(Team,pk= request.user.timeprofile.active_team_id,status=Team.ACTIVE)
    all_projects = team.projects.all()
    members = team.members.all()

    num_days = int(request.GET.get('num_days',0))
    date_user = datetime.now()- timedelta(days = num_days)
    date_entries = Entry.objects.filter(team=team,created_by=request.user,created_at__date=date_user,is_track=True)


    #month pagination
    user_num_months = int(request.GET.get('user_num_months',0))
    user_month = datetime.now()-relativedelta(months=user_num_months)

    for project in all_projects:
        project.get_time_for_user_and_project_and_month = get_time_for_user_and_project_and_month(team,project,request.user,user_month)

    

    context = {
        'team':team,
        'all_projects':all_projects,
        'date_entries':date_entries,
        'num_days':num_days,
        'date_user':date_user,
        'members':members,
        'time_for_user_and_date':get_time_for_user_and_date(team,request.user,date_user),

        'user_num_months':user_num_months,
        'user_month':user_month,
        'time_for_user_and_month':get_time_for_uer_and_month(team,request.user,user_month),
        'time_for_user_and_date':get_time_for_user_and_date(team,request.user,date_user)


    }
    return render(request,template_name,context)
