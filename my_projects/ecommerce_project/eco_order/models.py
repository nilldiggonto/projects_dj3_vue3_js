from django.db import models

from ecommerce_project.eco_product.models import Product
from ecommerce_project.eco_vendor.models import Vendor
# Create your models here.
class Order(models.Model):
    first_name          = models.CharField(max_length=120)
    last_name           = models.CharField(max_length=120)
    email               = models.CharField(max_length=120)
    address             = models.CharField(max_length=120)
    zipcode             = models.CharField(max_length=10)
    place               = models.CharField(max_length=120)
    phone               = models.CharField(max_length=120)
    created_at          = models.DateTimeField(auto_now_add=True)
    paid_amount         = models.DecimalField(max_digits=8,decimal_places=2)
    vendors             = models.ForeignKey(Vendor,related_name='orders',on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    order       = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product     = models.ForeignKey(Product,related_name='items',on_delete=models.CASCADE)
    vendor      = models.ForeignKey(Vendor,related_name='items',on_delete=models.CASCADE)
    vendor_paid = models.BooleanField(default=False)
    price       = models.DecimalField(max_digits=8,decimal_places=2)
    quantity    = models.IntegerField(default=1)

    def __str__(self):
        return self.id

    def get_total_price(self):
        return self.price * self.quantity


    
