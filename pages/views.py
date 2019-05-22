from django.shortcuts import render
from django.http import HttpResponse
from experts.models import Expert
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/services.html')