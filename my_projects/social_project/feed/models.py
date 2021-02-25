from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Social(models.Model):
    body        = models.CharField(max_length=300)
    created_by  = models.ForeignKey(User,on_delete=models.CASCADE,related_name='socials')
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
