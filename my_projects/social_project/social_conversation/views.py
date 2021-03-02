from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Conversation,ConversationMessage
# Create your views here.

@login_required
def conversationView(request):
    tempalte_name = 'conversation/conversation.html'
    converse = request.user.conversations.all()

    context = {
        'converse':converse,
    }
    return render(request,tempalte_name,context)
