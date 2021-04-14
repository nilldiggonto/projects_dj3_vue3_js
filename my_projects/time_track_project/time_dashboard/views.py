from django.shortcuts import render,redirect,get_object_or_404
from datetime import datetime,timedelta,timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from dateutil.relativedelta import relativedelta

from time_track_project.time_task.models import ProjectTask
from time_track_project.time_team.models import Team

# Create your views here.

@login_required
def timeDashboard(request):
    template_name = 'time_dashboard/dashboard.html'
    return render(request,template_name)
