from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def feedView(request):
    template_name ='feed/feed.html'
    return render(request,template_name)