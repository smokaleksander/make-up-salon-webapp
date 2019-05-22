from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    img = models.ImageField(upload_to='icons')
    def __str__(self):
        return self.name
