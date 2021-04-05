from django.urls import path
from .views import add_team,team,edit_team

urlpatterns = [
    path('add/',add_team,name='time-add-team'),
    path('edit/',edit_team,name='time-edit-team'),
    path('<int:team_id>/',team,name='time-team-details'),

]