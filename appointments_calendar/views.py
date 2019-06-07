from django.shortcuts import render
from .models import Appointment
from pytz import timezone, utc
from django.conf import settings
from .choices import expert_choices
TZ = timezone(settings.TIME_ZONE)


def utcisoformat(dt):
    """
    Return a datetime object in ISO 8601 format in UTC, without microseconds
    or time zone offset other than 'Z', e.g. '2011-06-28T00:00:00Z'. Useful
    for making Django DateTimeField values compatible with the
    jquery.localtime plugin.
    """
    # Convert datetime to UTC, remove microseconds, remove timezone, convert to string
    return TZ.localize(dt.replace(microsecond=0)).astimezone(utc).isoformat() + 'Z'

def booking(request):
    appointments= Appointment.objects.all()
    worker=list(expert_choices.keys())[0]
    print(worker)
    appointments=appointments.filter(worker=worker)
    for app in appointments:
        app.start_time=app.start_time.isoformat()
        app.end_time=app.end_time.isoformat()
    context={
        'appointments':appointments,
        'expert_choices':expert_choices,
    }
    return render(request, 'appointments_calendar/calendar.html', context)

def filter(request):
    if 'worker' in request.GET:
        worker = request.GET['worker']
        print(worker)
        appointments= Appointment.objects.all()
        appointments=appointments.filter(worker=worker)
    for app in appointments:
        app.start_time=app.start_time.isoformat()
        app.end_time=app.end_time.isoformat()
    context={
        'appointments':appointments,
        'expert_choices':expert_choices,
    }
    return render(request, 'appointments_calendar/calendar.html', context)
