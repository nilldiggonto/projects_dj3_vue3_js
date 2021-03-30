from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user    = models.ForeignKey(User,related_name='timeprofile',on_delete=models.CASCADE)
    active_team_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username)
