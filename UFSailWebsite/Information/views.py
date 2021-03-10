from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'current_item' : 'home'
    }
    return render(request, 'Information/home.html', context)

def contact(request):
    context = {
        'current_item' : 'contact'
    }
    return render(request, 'Information/contact.html', context)

def events(request):
    context = {
        'current_item' : 'events'
    }
    return render(request, 'Information/events.html', context)