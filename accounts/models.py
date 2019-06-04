from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDERS=(
        ('male','Male'),
        ('female','Female'),
    )
    gender=models.CharField(max_length=6, choices=GENDERS, blank=True)
    phone_num=models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
