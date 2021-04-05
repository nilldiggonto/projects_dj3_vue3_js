from django.urls import path
from .views import add_team,team

urlpatterns = [
    path('add/',add_team,name='time-add-team'),
    path('<int:team_id>/',team,name='time-team-details'),
]