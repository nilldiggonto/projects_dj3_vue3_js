from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Vendor
from django.contrib.auth.decorators import login_required


from ecommerce_project.eco_product.models import Category,Product

from .forms import ProductForm
from django.utils.text import slugify
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

@login_required
def vendorView(request):
    template_name = 'vendor/vendor_admin.html'
    vendor = request.user.vendor
    products = vendor.products.all()
    orders = vendor.orders.all()
    for order in orders:
        order.vendor_amount = 0 
        order.vendor_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:
                    order.vendor_paid_amount += item.get_total_price()
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid = False

    return render(request,template_name,{'vendor':vendor,'products':products,'orders':orders})

@login_required
def add_product(request):
    template_name = 'vendor/add_product.html'
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('eco-vendor-admin')
    else:
        form = ProductForm()
    return render(request,template_name,{'form':form})



@login_required
def edit_vendor(request):
    vendor = request.user.vendor

    if request.method == 'POST':
        name = request.POST.get('name','')
        email   = request.POST.get('email','')

        if name:
            vendor.created_by.email = email
            vendor.created_by.save()

            vendor.name = name
            vendor.save()

            return redirect('eco-vendor-admin')
    return render(request,'vendor/edit_vendor.html',{'vendor':vendor})
    
