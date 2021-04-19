from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user    = models.OneToOneField(User,related_name='timeprofile',on_delete=models.CASCADE)
    active_team_id = models.IntegerField(default=0)
    avatar  = models.ImageField(upload_to = 'time/avatars/',blank=True,null=True)

    def __str__(self):
        return str(self.user.username)

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return 'https://i.pinimg.com/originals/7d/eb/0d/7deb0db7a4928366eab74e5a09bb24f2.png'
