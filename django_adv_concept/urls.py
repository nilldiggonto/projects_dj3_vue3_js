
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Teacher Student Council' #admin stie name change
admin.site.index_title = 'Mangage the student and techaer classes'
