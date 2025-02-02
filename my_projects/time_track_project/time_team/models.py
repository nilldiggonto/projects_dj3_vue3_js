from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Team(models.Model):
    #status
    ACTIVE = 'active'
    DELETED = 'deleted'
    CHOICES_STATUS = (
        (ACTIVE,'Active'),
        (DELETED,'Deleted')
    )

    title       =   models.CharField(max_length=230)
    members     =   models.ManyToManyField(User,related_name='teams')
    created_by  =   models.ForeignKey(User,related_name='created_teams',on_delete=models.CASCADE)
    created_at  =   models.DateTimeField(auto_now_add=True)
    status      =   models.CharField(max_length=10,choices=CHOICES_STATUS,default=ACTIVE)

    class Meta:
        ordering = ['title',]
    def __str__(self):
        return self.title


#invite
class Invitation(models.Model):
    INVITED = 'invited'
    ACCEPTED = 'accepted'

    CHOICES_STATUS =(
        (INVITED,'Invited'),
        (ACCEPTED,'Accepted')
    )

    team    = models.ForeignKey(Team,related_name='invitations', on_delete=models.CASCADE)
    email   = models.EmailField()
    code    = models.CharField(max_length=120)
    status  = models.CharField(max_length=120,choices=CHOICES_STATUS,default=INVITED)
    date_sent   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

