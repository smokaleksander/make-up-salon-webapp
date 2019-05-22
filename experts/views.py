from django.shortcuts import render
from .models import Expert
# Create your views here.

def index(request):
    experts= Expert.objects.all()

    context={
        'experts': experts
    }
    return render(request, 'experts/experts.html', context)