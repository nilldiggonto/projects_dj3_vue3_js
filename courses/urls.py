from django.urls import path
from .views import ClassSelectFormView,AddClassFormView

app_name = 'course'

urlpatterns = [
    path('',ClassSelectFormView.as_view(),name='course-view'),
    path('add/',AddClassFormView.as_view(),name='add-class'),
]