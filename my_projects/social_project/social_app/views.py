from django.shortcuts import render

# Create your views here.
def test_view(request):
    template_name = 'social_app/social.html'
    return render(request,template_name)