from django.shortcuts import render,get_object_or_404,redirect
import random
from django.db.models import Q
from .forms import AddToCartForm
from django.contrib import messages

from ecommerce_project.eco_cart.cart import Cart

# Create your views here.
from .models import Category,Product

def productDetail(request,category_slug,product_slug):
    product = get_object_or_404(Product,category__slug=category_slug,slug =product_slug)

    #cart
    cart = Cart(request)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)


        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            print(quantity)
            print(quantity)
            print(quantity)
            print(quantity)

            cart.add(product_id=product.id,quantity=quantity,update_quantity=True)
            messages.success(request,'Product added to cart')
            return redirect('eco-p-detail', category_slug=category_slug,product_slug=product_slug)
    else:
        form = AddToCartForm()


    ##
    

    similar_products = list(product.category.products.exclude(id=product.id))

    if (len(similar_products)>4):
        similar_products = random.sample(similar_products,4)
    
    template_name = 'product/product.html'
    context = {
        'product':product,
        'similar_products':similar_products,
        'form':form,
    }
    return render(request,template_name,context)


def category(request,category_slug):
    template_name = 'product/category.html'
    category = get_object_or_404(Category, slug=category_slug)

    return render(request,template_name,{'category':category,})



#search
def search(request):
    query = request.GET.get('q','')
    products = Product.objects.filter(Q(title__icontains=query)| Q(description__icontains=query))

    template_name = 'product/search.html'
    return render(request,template_name,{'products':products,'query':query})