from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Social
from django.contrib.auth.models import User
# Create your views here.
@login_required
def feedView(request):
    userids = [request.user.id]
    for s in request.user.SocialProfile.follows.all():
        userids.append(s.user.id)

    socials  = Social.objects.filter(created_by_id__in = userids)
    context = {
        'socials':socials,
    }
    template_name ='feed/feed.html'
    return render(request,template_name,context)


#search
def searchView(request):
    query = request.GET.get('query','')

    if (len(query)>0):
        socials = User.objects.filter(username__icontains=query)
    else:
        socials = []
    
    context = {
        'query':query,
        'socials':socials,
    }
    template_name = 'feed/search.html'
    return render(request,template_name,context)