from datetime import datetime

from time_track_project.time_task.models import ProjectTask,Entry
from time_track_project.time_team.models import Team

def get_time_for_user_and_date(team,user,date):
    entries = Entry.objects.filter(team=team,created_by=user,created_at__date=date,is_track=True)

    return sum(entry.minutes for entry in entries)

def get_time_for_team_and_month(team,month):
    entries = Entry.objects.filter(team=team,created_at__year = month.year, created_at__month=month.month, is_track=True)
    return sum(entry.minutes for entry in entries)

def get_time_for_uer_and_month(team,user,month):
    entries = Entry.objects.filter(team=team,created_by=user,created_at__year = month.year, created_at__month=month.month, is_track=True)
    return sum(entry.minutes for entry in entries)

def get_time_for_user_and_project_and_month(team,project,user,month):
    entires = Entry.objects.filter(team=team,project=project,created_by=user,created_at__year = month.year, created_at__month=month.month, is_track=True)
    return sum(entry.minutes for entry in entires)

def get_time_for_user_and_team_month(team,user,month):
    entries = Entry.objects.filter(team=team,created_by = user,created_at__year = month.year, created_at__month=month.month, is_track=True)
    return sum(entry.minutes for entry in entries)
