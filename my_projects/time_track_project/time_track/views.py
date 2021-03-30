from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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

