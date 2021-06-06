from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy

from .models import ClassDuration,CourseInfo,PrefectStudent
from .forms import ClassDurationForm,CourseInfoForm,ClassSelectForm
# Create your views here.

class ClassSelectFormView(FormView):
    form_class= ClassSelectForm
    template_name = 'courses/main.html'
    success_url = reverse_lazy('course:add-class')

    def post(self,*args,**kwargs):
        self.request.session['class_name'] = self.request.POST.get('class_name').lower().capitalize()
        return super().post(*args,**kwargs)

class AddClassFormView(FormView):
    template_name = 'courses/add.html'
    success_url = reverse_lazy('home-page')

    def get_form_class(self,*args,**kwargs):
        movie = self.request.session.get('class_name')
        if movie == 'Student':
            return ClassDurationForm
        else:
            return CourseInfoForm
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

