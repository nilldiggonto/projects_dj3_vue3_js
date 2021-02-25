from django.shortcuts import render

# Create your views here.
def social_frontpage(request):
    template_name = 'social_app/social.html'
    return render(request,template_name)