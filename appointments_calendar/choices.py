from .models import Expert

experts= Expert.objects.all()
expert_choices={}
for e in experts:
    expert_choices[e]=e.id