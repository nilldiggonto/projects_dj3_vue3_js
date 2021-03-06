from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Vendor
from django.contrib.auth.decorators import login_required
# Create your views here.
#
@login_required
def become_vendor(request):
    template_name = 'vendor/become_vendor.html'

    # if not Vendor.objects.filter(created_by=request.user).exists:

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     user = form.save()
        #     login(request,user)
        vendor_name = request.POST.get('vendor')
        if Vendor.objects.filter(created_by=request.user).exists():
            return redirect('eco-home')
        else:


            vendor = Vendor.objects.create(name=vendor_name,created_by=request.user)
            return redirect('eco-home')

        
    else:
        form = UserCreationForm()

    return render(request,template_name,{'form':form})
    # # else:
    #     return redirect('eco-home')
