from django.urls import path
from .views import time_projects,time_projectDetail,time_projectEdit,task_detail,task_edit,edit_entry,delete_entry

urlpatterns = [
    path('',time_projects,name='time-projects-list'),
    path('detail/<int:project_id>/',time_projectDetail,name='time-project-detail'),
    path('edit/<int:project_id>/',time_projectEdit,name='time-project-edit'),

    path('task/<int:project_id>/<int:task_id>/',task_detail,name='time-task-detail'),
    path('task/edit/<int:project_id>/<int:task_id>/',task_edit,name='time-task-edit'),

    path('edit/entry/<int:project_id>/<int:task_id>/<int:entry_id>/',edit_entry,name='time-edit-entry'),
    path('delete/entry/<int:project_id>/<int:task_id>/<int:entry_id>/',delete_entry,name='time-delete-entry'),


]