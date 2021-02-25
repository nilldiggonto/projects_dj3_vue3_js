from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Social
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