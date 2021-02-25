from django.shortcuts import render

def home_view(request):
    template_name = 'my_projects/home.html'

    return render(request,template_name)

def project_list(request):
    template_name ='my_projects/project_list.html'
    return render(request,template_name)