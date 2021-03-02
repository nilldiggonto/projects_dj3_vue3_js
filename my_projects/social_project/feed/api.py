import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Social,Like

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
    print(data)
    print(data)
    print(data)
    print(data)

    social_id = data['social_id']

    if not Like.objects.filter(social_id= social_id).filter(created_by=request.user).exists():
        like = Like.objects.create(social_id=social_id,created_by = request.user)

    json_response = {'success':True}

    return JsonResponse(json_response)