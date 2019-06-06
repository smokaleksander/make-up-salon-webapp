from django.db import models
from experts.models import Expert
from services.models import Service
from accounts.models import User

class Appointment(models.Model):
    worker=models.ForeignKey(Expert, on_delete=models.PROTECT)
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    service_type=models.ForeignKey(Service, on_delete=models.PROTECT)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    added=models.DateTimeField(auto_now_add=True)
    note=models.TextField(max_length=100, blank=True)
    def __str__(self):
        return str(self.service_type)
