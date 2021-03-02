from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Conversation(models.Model):
    users       = models.ManyToManyField(User,related_name='conversations')
    modified_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-modified_at']

    def __str__(self):
        return str(self.users)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation,related_name='messages', on_delete=models.CASCADE)
    content      = models.CharField(max_length=300)
    created_at   = models.DateTimeField(auto_now_add=True)
    created_by   = models.ForeignKey(User,related_name='messages',on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

    def save(self,*args,**kwargs):
        self.conversation.save()
        super(ConversationMessage,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.created_by)
