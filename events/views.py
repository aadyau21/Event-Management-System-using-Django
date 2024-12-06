from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

@login_required
def dashboard(request):
    if request.user.role == 'Organizer':
        events = request.user.organized_events.all()
    else:
        events = Event.objects.exclude(attendees=request.user)
    return render(request, 'events/dashboard.html', {'events': events})

@login_required
def create_event(request):
    if request.user.role != 'Organizer':
        return redirect('dashboard')
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('dashboard')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user.role == 'Attendee':
        event.attendees.add(request.user)
    return redirect('dashboard')
