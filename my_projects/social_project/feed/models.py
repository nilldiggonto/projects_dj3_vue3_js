from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Social(models.Model):
    body        = models.CharField(max_length=300)
    created_by  = models.ForeignKey(User,on_delete=models.CASCADE,related_name='socials')
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class Like(models.Model):
    social      = models.ForeignKey(Social,related_name='likes', on_delete=models.CASCADE)
    created_by  = models.ForeignKey(User,related_name='likes', on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_by)
