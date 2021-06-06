from django.db import models

# Create your models here.
class Student(models.Model):
    name        = models.CharField(max_length=120)
    is_topper   = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)