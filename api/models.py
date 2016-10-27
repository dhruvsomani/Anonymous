from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class KeyLogRecord(models.Model):
    user = models.ManyToManyField(User)
    string = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField(default=datetime.datetime(2037, 12, 31))
    quality = models.CharField(max_length=8, default='white')
    starred = models.BooleanField(default=False)

    def __str__(self):
        return self.string


class Screenshot(models.Model):
    user = models.ManyToManyField(User)
    img_string = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return user.username


admin.site.register(KeyLogRecord)
admin.site.register(Screenshot)