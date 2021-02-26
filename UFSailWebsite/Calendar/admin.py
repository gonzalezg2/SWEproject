from django.contrib import admin
from .models import Event

# Make events editable by admins
admin.site.register(Event)