from django.conf import settings
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.core.mail import send_mail

def contact(request):
        if request.method =="POST":
                name=request.POST.get("name")
                email=request.POST.get("email")
                subject=request.POST.get("subject")
                message=request.POST.get("message")
                
                #sendgrid mail sending
               

                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,[ settings.EMAIL_HOST_USER,], fail_silently=False)

                return redirect('contact')
        else:
                return render(request, 'contact_form/contact.html')