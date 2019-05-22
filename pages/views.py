from django.shortcuts import render
from django.http import HttpResponse
from experts.models import Expert
from services.models import Service

def index(request):
    experts=Expert.objects.all()
   
    services= Service.objects.all()

    context={
        'services':services,
        'experts':experts
    }
    return render(request, 'pages/index.html', context)
