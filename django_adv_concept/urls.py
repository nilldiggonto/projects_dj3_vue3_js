from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from .views import home_view,login_view,logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home-page'),
    path('course/',include('courses.urls',namespace='course')),
    path('users/',include('users.urls',namespace='users')),

    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




admin.site.site_header = 'Teacher Student Council' #admin stie name change
admin.site.index_title = 'Mangage the student and techaer classes'
