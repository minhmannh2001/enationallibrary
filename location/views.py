from django.shortcuts import render
from .models import Event


def event_wrapper(request):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    events = Event.objects.all()
    numOfEvents = len(list(events)) * 280
    return render(request, 'events/event.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'events': events,
        'numOfEvents': numOfEvents,
    })


def event_detail(request, slug):
    is_login = False
    is_staff = False
    if not request.user.is_anonymous:
        is_login = True
    if request.user.is_staff:
        is_staff = True
    event = Event.objects.get(slug=slug)
    events = Event.objects.all()[0:6]
    return render(request, 'events/event-detail.html', {
        'is_login': is_login,
        'is_staff': is_staff,
        'user': request.user,
        'event': event,
        'events': events,
    })
