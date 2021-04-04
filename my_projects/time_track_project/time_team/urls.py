from django.urls import path
from .views import add_team

urlpatterns = [
    path('add/',add_team,name='time-add-team'),
]