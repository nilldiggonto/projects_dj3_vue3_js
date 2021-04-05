from time_track_project.time_team.models import Team

def active_team(request):
    if request.user.is_authenticated:
        if request.user.timeprofile.active_team_id:
            # team = 'ok'
            team = Team.objects.get(pk=request.user.timeprofile.active_team_id)
            return {'active_team':team}
    return {'active_team':None}