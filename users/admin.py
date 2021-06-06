from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
      *UserAdmin.fieldsets,
      (
          'User role',
          {
              'fields': (
                  'is_teacher',
                  'is_student',
              )
          }
      )
    )
    

admin.site.register(CustomUser,CustomUserAdmin)
