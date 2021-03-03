from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Conversation,ConversationMessage
from django.contrib.auth.models import User
# Create your views here.

@login_required
def conversationView(request):
    tempalte_name = 'conversation/conversation.html'
    converse = request.user.conversations.all()

    context = {
        'converse':converse,
    }
    return render(request,tempalte_name,context)


@login_required
def conversationRecipient(request,user_id):
    template_name = 'conversation/conversation.html'
    conversations = Conversation.objects.filter(users__in=[request.user.id])
    conversations = conversations.filter(users__in=[user_id])

    if conversations.count() ==1:
        conversation = conversations[0]
    
    else:
        recipient = User.objects.get(pk=user_id)
        conversation = Conversation.objects.create()
        conversation.users.add(request.user)
        conversation.users.add(recipient)
        conversation.save()
    return render(request,template_name,{'conversation':conversation})

