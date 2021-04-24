from datetime import datetime,time,timezone
from django.shortcuts import get_object_or_404
from .models import Entry
from time_track_project.time_team.models import Team

def active_entry(request):
    if request.user.is_authenticated:
        if request.user.timeprofile.active_team_id:
            team= get_object_or_404(Team,pk=request.user.timeprofile.active_team_id,status=Team.ACTIVE)
            untracked_entries = Entry.objects.filter(team=team,created_by=request.user,minutes=0,is_track=False)

            if untracked_entries:
                active_entry = untracked_entries.first()
                active_entry.seconds_since = int((datetime.now(timezone.utc) - active_entry.created_at).total_seconds())

                return {'active_entry_seconds':active_entry.seconds_since,'start_time':active_entry.created_at.isoformat()}
    return {'active_entry_seconds':0, 'start_time':datetime.now().isoformat()}