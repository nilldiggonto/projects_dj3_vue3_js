from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ecommerce_project.eco_vendor.models import Vendor

# Create your views here.
@login_required
def ecoView(request):
    template_name= 'ecommerce/eco.html'
    # if 
    vendor = None
    if Vendor.objects.filter(created_by=request.user).exists():
        vendor = Vendor.objects.get(created_by=request.user)
        # print(vendor)
        # print(vendor)
        # print(vendor)
        # print(vendor)
        # print(vendor)
        # print(vendor)
    # else:

    return render(request,template_name,{'vendor':vendor})