from django.contrib import admin
from .models import *
from students.models import Student
# Register your models here.
class CourseDurationAdmin(admin.ModelAdmin):
    def render_change_form(self,request,context,*args,**kwargs):
        context['adminform'].form.fields['students'].queryset= Student.objects.filter(is_topper=True)
        return super().render_change_form(request,context,*args,**kwargs)

class CourseInfoAdmin(admin.ModelAdmin):
    def render_change_form(self,request,context,*args,**kwargs):
        context['adminform'].form.fields['students'].queryset= Student.objects.filter(is_topper=False)
        return super().render_change_form(request,context,*args,**kwargs)

admin.site.register(ClassDuration,CourseDurationAdmin)
admin.site.register(CourseInfo,CourseInfoAdmin)