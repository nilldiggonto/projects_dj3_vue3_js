from django.db import models
from students.models import Student
# Create your models here.
class PrefectStudent(models.Model):
    title       = models.CharField(max_length=120)
    students    = models.ManyToManyField(Student,blank=True,null=True)
    date        = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return str(self.title)
    class Meta:
        abstract = True
    
class ClassDuration(PrefectStudent):
    length = models.CharField(max_length=120)

    def __str__(self):
        return str(self.length)

class NormalStudent(models.Model):
    class_belong = models.CharField(max_length=120)

    def __str__(self):
        return str(self.class_belong)
