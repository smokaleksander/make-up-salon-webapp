from django.shortcuts import render, redirect
from django.contrib import messages
from djnago.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        phone= request.POST['phone']
        gender= request.POST['gender']
        email= request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        #if password == password2:
            #if User.objects.filter()
        #else:
            #messages.error(request, 'Passwords do not match')
            #return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        return 
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('index')