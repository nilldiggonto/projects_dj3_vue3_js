from django.db import models

from io import BytesIO
from PIL import Image
from django.core.files import File

from ecommerce_project.eco_vendor.models import Vendor

# Create your models here.
class Category(models.Model):
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=250)
    ordering    = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']
    
    def __str__(self):
        return str(self.title)


class Product(models.Model):
    category    =   models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    vendor      =   models.ForeignKey(Vendor,related_name='products',on_delete=models.CASCADE)
    title       =   models.CharField(max_length=200)
    slug        =   models.SlugField(max_length=255)
    description =   models.TextField(blank=True)
    price       =   models.DecimalField(max_digits=6,decimal_places=2)
    date_added  =   models.DateTimeField(auto_now_add=True)
    image       =   models.ImageField(upload_to='eco/uploads/',blank=True,null=True)
    thumbnail   =   models.ImageField(upload_to='eco/uploads/thumb/',blank=True,null=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return str(self.title)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://www.carnival.com/_ui/responsive/ccl/assets/images/notfound_placeholder.svg'

    def make_thumbnail(self,image,size=(300,200)):
        img     = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io,'JPEG',quality=85)

        thumbnail = File(thumb_io,name=image.name)
        return thumbnail       