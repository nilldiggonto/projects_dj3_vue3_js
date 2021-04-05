from django.urls import path
from .views import add_team,team,edit_team,activate_team

urlpatterns = [
    path('add/',add_team,name='time-add-team'),
    # path
    path('edit/',edit_team,name='time-edit-team'),
    path('activate_team/<int:team_id>/',activate_team,name='time-activate-team'),
    path('<int:team_id>/',team,name='time-team-details'),

]