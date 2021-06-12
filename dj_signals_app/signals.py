from django.db.models.signals import post_save,pre_save,m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from users.models import CustomUser
from .models import CarBuyer,Car,Order
import uuid

@receiver(post_save,sender=CustomUser)
def post_save_create_buyer(sender,instance,created,**kwargs):
    if created:
        CarBuyer.objects.create(user= instance)


@receiver(pre_save,sender=Car)
def pre_save_create_code(sender,instance,**kwargs):
    if instance.code =='':
        instance.code = str(uuid.uuid4()).replace('-','').upper()[:10]
    
    obj = CarBuyer.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()

@receiver(m2m_changed,sender=Order.cars.through)
def m2m_changed_car_order(sender,instance,action,**kwargs):
    total = 0
    total_price = 0 
    if action == 'post_add' or action == 'post_remove':
        for car in instance.cars.all():
            total +=1
            total_price += car.price
        instance.total = total
        instance.total_price = total_price
        instance.save()