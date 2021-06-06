from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request,'main/home.html')

def login_view(request):
    error_message = None
    form = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_teacher==True:
            login(request,user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('home-page')
        else:
            error_message = 'you are not the user'

    return render(request,'main/login.html',{'form':form,'error_msg':error_message})

def logout_view(request):
    logout(request)
    return redirect('home-page')