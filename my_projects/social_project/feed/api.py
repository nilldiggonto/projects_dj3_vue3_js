import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Social

@login_required
def api_add_feed(request):
    data = json.loads(request.body)
    body = data['body']

    social =Social.objects.create(body=body,created_by= request.user)
    return JsonResponse({'success':True})