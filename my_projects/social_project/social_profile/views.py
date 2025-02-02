from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import SocialProfileForm

from social_project.social_notification.utils import create_notification

# Create your views here.
@login_required
def socialprofileView(request,username):
    user = get_object_or_404(User,username=username)
    socials = user.socials.all()
    for social in socials:
        # print(social.likes)
        likes = social.likes.filter(created_by_id=request.user.id)

        if likes.count()>0:
            social.liked= True
        else:
            social.liked = False

    context = {
        'user':user,
        'socials':socials
    }
    template_name = 'social_profile/social_profile.html'

    return render(request,template_name,context)

@login_required
def follow_userView(request,username):
    user = get_object_or_404(User,username=username)

    request.user.SocialProfile.follows.add(user.SocialProfile)


    #notification
    create_notification(request,user,'follower')
    return redirect('social-profile', username=username)

@login_required
def unfollow_userView(request,username):
    user = get_object_or_404(User,username=username)

    request.user.SocialProfile.follows.remove(user.SocialProfile)
    return redirect('social-profile', username=username)


@login_required
def followerView(request,username):
    user = get_object_or_404(User,username=username)
    template_name = 'social_profile/social_follower.html'

    context = {'user':user,}


    return render(request,template_name,context)


@login_required
def followView(request,username):
    user = get_object_or_404(User,username=username)
    template_name = 'social_profile/social_follow.html'

    context = {'user':user,}


    return render(request,template_name,context)


#change the avatar
@login_required
def edit_avatarView(request):
    if request.method == 'POST':
        form = SocialProfileForm(request.POST,request.FILES,instance=request.user.SocialProfile)

        if form.is_valid():
            form.save()
            return redirect('social-profile', username=request.user.username)
        # else:
    else:
        form = SocialProfileForm(instance=request.user.SocialProfile)
    
    context = {
        'user':request.user,
        'form':form,
    }
    return render(request,'social_profile/edit_avatar.html',context)

