from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SocialProfile(models.Model):
    user    = models.OneToOneField(User,on_delete=models.CASCADE)
    follows = models.ManyToManyField('self',related_name='followed_by',symmetrical=False)


User.SocialProfile = property(lambda u:SocialProfile.objects.get_or_create(user=u)[0])
    
