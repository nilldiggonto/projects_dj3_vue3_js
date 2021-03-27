from django.shortcuts import render

# Create your views here.
def time_frontpage(request):
    tempalte_name = 'time_track/time_front.html'

    return render(request,tempalte_name)