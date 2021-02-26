from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField('event title', max_length=200)
    description = models.TextField('event description')
    start = models.DateTimeField('start time')
    end = models.DateTimeField('end time')

    # Get a human-readable representation of the object
    def __str__(self):
        return f"{self.title}: {self.description}"

    def has_passed(self):
    	return self.end <= timezone.now()
