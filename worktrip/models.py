import datetime
from django.db import models


class Venue(models.Model):
    # You want to create a set of tags/keywords
    # New ones can auto be added by people
    created_date = models.DateField(default=datetime.date.today)
    name = models.CharField(max_length=100, default="")
    # The speed in this element should be the average of all input speeds
    download_speed = models.IntegerField(default=0)
    upload_speed = models.IntegerField(default=0)
    # How can venue_type be a OneOfType value? AirBnB, Cafe, Bar, etc.
    venue_type = models.CharField(max_length=100, default="")
    venue_url = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["created_date"]
