from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notificationsView(request):
    goto = request.GET.get('goto','')
    notification_id = request.GET.get('notification',0)

    if goto !='':
        notifcation = Notification.objects.get(pk=notification_id)
        notifcation.is_read = True
        notifcation.save()

        if notifcation.notification_type == Notification.MESSAGE:
            return redirect('social-converse-one',user_id=notifcation.created_by.id)
        elif notifcation.notification_type == Notification.FOLLOWER:
            return redirect('social-profile',username=notifcation.created_by.username)
        elif notifcation.notification_type == Notification.LIKE:
            return redirect('social-profile',username=notifcation.to_user.username)
    return render(request,'notification/notification.html')
        