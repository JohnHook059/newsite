from django.db import models
from django.utils.timezone import now, pytz
from django.conf import settings

class Comment(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    text = models.CharField(max_length=1000000)
    time = models.DateTimeField(default=now().astimezone(pytz.timezone(settings.TIME_ZONE)))

    class Meta:
        ordering = ['-time']