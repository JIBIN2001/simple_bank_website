from django.db import models

# Create your models here.
class Formregister(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField()
    district = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    materials = models.CharField(max_length=250)

    def __str__(self):
        return self.name