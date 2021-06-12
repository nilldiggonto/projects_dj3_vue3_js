from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser
import uuid
# Create your models here.
class CarBuyer(models.Model):
    user        = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    from_signal = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class Car(models.Model):
    name    = models.CharField(max_length=120)
    price   = models.PositiveIntegerField()
    buyer   = models.ForeignKey(CarBuyer,on_delete=models.CASCADE)
    code    = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return f'{self.name}-{self.price}-{self.buyer}'

    # def save(self,*args,**kwargs):
    #     if self.code == '':
    #         self.code = str(uuid.uuid4()).replace('-','').upper()[:10]
    #     return super().save(*args,**kwargs)

class Order(models.Model):
    name        = models.CharField(max_length=200)
    cars        = models.ManyToManyField(Car)
    total       = models.PositiveIntegerField(blank=True,null=True)
    total_price = models.PositiveIntegerField(blank=True,null=True)
    active      = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)