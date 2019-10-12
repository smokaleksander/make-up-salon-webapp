from .models import Expert, Service

experts= Expert.objects.all()
expert_choices=experts

services=Service.objects.all()
service_choices=services
