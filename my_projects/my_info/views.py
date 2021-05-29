from django.shortcuts import render

# Create your views here.
def my_home(request):
    template_name = 'my_info/home.html'

    return render(request,template_name)