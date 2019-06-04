from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth 
from .models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        username=request.POST['username']
        phone= request.POST['phone']
        gender= request.POST['gender']
        email= request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'That email is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email, gender=gender, phone_num=phone)
                user.save()
                messages.success(request, 'Register successful')
                return redirect('login')
                

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password not correct')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('index')