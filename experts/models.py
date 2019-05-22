from django.db import models
from datetime import datetime

class Expert (models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    position = models.CharField(max_length=50, default='stylist')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description =  models.TextField(blank=False ,max_length=150)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    hire_date= models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name+' ' + self.lastname