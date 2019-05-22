from django.shortcuts import render
from django.http import HttpResponse
from experts.models import Expert

def index(request):
    experts=Expert.objects.all()
    context={
        'experts':experts
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/services.html')