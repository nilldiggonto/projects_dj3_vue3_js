from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import home_view,project_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='homepage'),
    path('project/list/',project_list,name='project-list'),

    path('social/',include('social_project.social_app.urls')),
    path('eco/',include('ecommerce_project.ecommerce_app.urls')),
    path('time/',include('time_track_project.time_track.urls'),)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
