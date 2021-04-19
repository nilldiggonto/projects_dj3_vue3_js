from django.urls import path
from .views import timeDashboard,timeView_user
urlpatterns = [
    path('',timeDashboard,name='time-dashboard'),
    path('user/<int:user_id>/',timeView_user,name='time-dashboard-user'),

]