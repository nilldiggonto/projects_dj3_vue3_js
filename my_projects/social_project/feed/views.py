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
    # print(socials)

    for social in socials:
        # print(social.likes)
        likes = social.likes.filter(created_by_id=request.user.id)

        if likes.count()>0:
            social.liked= True
        else:
            social.liked = False
    context = {
        'user':request.user,
        'socials':socials,
    }
    template_name ='feed/feed.html'
    return render(request,template_name,context)


#search
def searchView(request):
    query = request.GET.get('query','')

    if (len(query)>0):
        socials = User.objects.filter(username__icontains=query)
        socials_feeds = Social.objects.filter(body__icontains=query)
    else:
        socials = []
        socials_feeds = []

    
    context = {
        'query':query,
        'socials':socials,
        'socials_feeds':socials_feeds
    }
    template_name = 'feed/search.html'
    return render(request,template_name,context)