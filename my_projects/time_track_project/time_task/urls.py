from django.urls import path
from .views import time_projects,time_projectDetail

urlpatterns = [
    path('',time_projects,name='time-projects-list'),
    path('detail/<int:project_id>/',time_projectDetail,name='time-project-detail'),
]