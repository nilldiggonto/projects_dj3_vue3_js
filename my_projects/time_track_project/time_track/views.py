from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def time_frontpage(request):
    tempalte_name = 'time_track/time_front.html'

    return render(request,tempalte_name)

@login_required
def time_account(request):
    template_name = 'time_track/time_account.html'
    user = request.user
    context = {
        'user':user
    }
    return render(request,template_name,context)

@login_required
def time_edit_profile(request):
    template_name = 'time_track/time_edit_profile.html'
    user = request.user


    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email','')
        request.user.save()

        messages.info(request,'Profile edit successfull')
        return redirect('time-account')
    return render(request,template_name,{'user':user})


