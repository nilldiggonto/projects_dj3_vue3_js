from django.shortcuts import render

# Create your views here.
def ecoView(request):
    template_name= 'ecommerce/eco.html'
    return render(request,template_name)