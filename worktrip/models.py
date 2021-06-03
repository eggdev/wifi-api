import datetime
from django.db import models


class Location(models.Model):
    created_date = models.DateField(default=datetime.date.today)
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["created_date"]
