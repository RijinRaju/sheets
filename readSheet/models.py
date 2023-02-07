from msilib.schema import Class
from statistics import mode
from django.db import models

# Create your models here.


class Data(models.Model):
    first_name = models.CharField(max_length=150,null=True)
    last_name = models.CharField(max_length=150,null=True)
    Gender = models.CharField(max_length=150,null=True)
    country = models.CharField(max_length=150,null=True)
    age = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=False,null=True)
    eid = models.IntegerField(null=True)


    def __str__(self):
        return self.first_name
