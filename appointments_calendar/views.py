from django.shortcuts import render, redirect
from .models import Appointment
from accounts.models import User
from pytz import timezone, utc
from django.conf import settings
from .choices import expert_choices, service_choices
import random
import datetime

def booking(request):
    appointments= Appointment.objects.all()
    if 'worker_choice' in request.GET:
        worker=request.GET['worker_choice']
        appointments=appointments.filter(worker__id=worker)
        worker=int(worker)
    else:
        worker=random.choice(expert_choices)
        worker=worker.id
        
        appointments=appointments.filter(worker_id=worker)

    for app in appointments:
        app.start_time=app.start_time.isoformat()
        app.end_time=app.end_time.isoformat()

    context={
        'appointments':appointments,
        'expert_choices':expert_choices,
        'service_choices':service_choices,
        'choosen_worker':worker  
    }
    return render(request, 'appointments_calendar/calendar.html', context)

def book(request):
    print('book method')
    if request.method == 'POST':
        worker=request.POST['worker']
        service_type=request.POST['service']
        time_start=request.POST['time_start']
        time_end=request.POST['time_end']
        
    user=request.user
     
    #customer=request.POST['firstname'] 
    #added=request.POST['firstname']
    #end_time=request.POST['firstname']
    #note=request.POST['firstname']

    
    for i in expert_choices:
        if worker == str(i.name+" "+i.lastname):
            worker=i.id
            break

    a=Appointment(worker_id=worker, customer_id=user.id, service_type_id=service_type, start_time=time_start, end_time=time_end, added=datetime.datetime.now() )
    a.save()

    appointments= Appointment.objects.all()
    appointments=appointments.filter(worker__id=worker)
    
    for app in appointments:
        app.start_time=app.start_time.isoformat()
        app.end_time=app.end_time.isoformat()
    context={
        'appointments':appointments,
        'expert_choices':expert_choices,
        'service_choices':service_choices,
        'choosen_worker':worker  
    }
    return redirect('/booking/', context)
