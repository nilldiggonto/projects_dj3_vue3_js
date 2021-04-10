from django.contrib import admin

# Register your models here.
from .models import ProjectTask,TaskPrimary,Entry

admin.site.register(ProjectTask)
admin.site.register(TaskPrimary)
admin.site.register(Entry)