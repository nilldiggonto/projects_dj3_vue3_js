from django.shortcuts import render,redirect
from .cart import Cart
import stripe

from django.conf import settings
from django.contrib import messages
from .forms import CheckoutForm

from ecommerce_project.eco_order.utils import checkout
# Create your views here.
def cart_detail(request):
    cart = Cart(request)
    tempalte_name = 'cart/cart.html'
    form = CheckoutForm()
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe_token = form.cleaned_data['stripe']
            charge = stripe.Charge.create(
                amount = int(cart.get_total_cost() * 100),
                currency = 'USD',
                description = 'somekinda charge',
                source = stripe_token
            )

            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            email       = form.changed_data['email']
            phone       = form.cleaned_data['phone']
            address     = form.cleaned_data['address']
            zipcode     = form.cleaned_data['zipcode']
            place       = form.cleaned_data['place']

            order = checkout(request,first_name,last_name,email,address,zipcode,place,phone,cart.get_total_cost())

            cart.clear()
            # pass
            return redirect('eco-cart-success')
    else:
        form = CheckoutForm()



    remove_from_cart = request.GET.get('remove_from_cart','')
    change_quantity = request.GET.get('change_quantity','')
    quantity = request.GET.get('quantity',0)





    if remove_from_cart:
        cart.remove(remove_from_cart)
        return redirect('eco-cart')

    if change_quantity:
        cart.add(change_quantity,quantity,True)

        return redirect('eco-cart')
    return render(request,tempalte_name,{'form':form,'stripe_pub_key':settings.STRIPE_PUB_KEY})



def order_success(request):
    return render(request,'cart/success.html')