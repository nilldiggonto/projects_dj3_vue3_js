import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Social,Like

from social_project.social_notification.utils import create_notification


@login_required
def api_add_feed(request):
    data = json.loads(request.body)
    body = data['body']

    social =Social.objects.create(body=body,created_by= request.user)
    return JsonResponse({'success':True})


@login_required
def api_add_like(request):
    # print(request)
    # print(request)
    # print(request)
    # print(request)

    data = json.loads(request.body)
    # print(data)
    # print(data)
    # print(data)
    # print(data)

    social_id = data['social_id']

    if not Like.objects.filter(social_id= social_id).filter(created_by=request.user).exists():
        like = Like.objects.create(social_id=social_id,created_by = request.user)


        #notification
        social = Social.objects.get(pk=social_id)

        create_notification(request,social.created_by,'lik')

    json_response = {'success':True}

    return JsonResponse(json_response)