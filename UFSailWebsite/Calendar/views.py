from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Event
from .custom_calendar import Calendar
import calendar
from django.utils.safestring import mark_safe

# Create your views here.
def index(request):
    latest = Event.objects.order_by('start')[:5]
    context = {'latest': latest}
    return render(request, 'calendar/test.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'calendar/detail.html', {'event': event})

def cal(request):
    cal = Calendar(calendar.SUNDAY)
    html_cal = cal.formatmonth(2020, 3)
    # return HttpResponse(html_cal)
    return render(request, 'calendar/cal.html', {'calendar': mark_safe(html_cal)})