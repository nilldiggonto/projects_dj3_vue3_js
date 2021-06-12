from django.db import models
# from django.contrib.auth.models import User
from users.models import CustomUser
# Create your models here.
class CarBuyer(models.Model):
    user        = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    from_signal = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)