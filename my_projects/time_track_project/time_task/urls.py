from django.urls import path
from .views import time_projects,time_projectDetail,time_projectEdit,task_detail,task_edit,edit_entry,delete_entry


from .api import api_discard_timer,api_start_timer,api_stop_timer
urlpatterns = [
    path('',time_projects,name='time-projects-list'),
    path('detail/<int:project_id>/',time_projectDetail,name='time-project-detail'),
    path('edit/<int:project_id>/',time_projectEdit,name='time-project-edit'),

    path('task/<int:project_id>/<int:task_id>/',task_detail,name='time-task-detail'),
    path('task/edit/<int:project_id>/<int:task_id>/',task_edit,name='time-task-edit'),

    path('edit/entry/<int:project_id>/<int:task_id>/<int:entry_id>/',edit_entry,name='time-edit-entry'),
    path('delete/entry/<int:project_id>/<int:task_id>/<int:entry_id>/',delete_entry,name='time-delete-entry'),


    path('api/start_timer/',api_start_timer,name='api-start-timer'),
    path('api/stop_timer/',api_stop_timer,name='api-stop-timer'),
    path('api/discard_timer/',api_discard_timer,name='api-discard-timer'),



]