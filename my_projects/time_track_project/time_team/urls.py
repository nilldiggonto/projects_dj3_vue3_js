from django.urls import path
from .views import add_team,team,edit_team,activate_team,inviteView,accept_invitation

urlpatterns = [
    path('add/',add_team,name='time-add-team'),
    # path
    path('edit/',edit_team,name='time-edit-team'),
    path('invite/',inviteView,name='time-team-invite'),

    path('accept/invite/',accept_invitation,name='time-accept-invite'),


    path('activate_team/<int:team_id>/',activate_team,name='time-activate-team'),
    path('<int:team_id>/',team,name='time-team-details'),

]