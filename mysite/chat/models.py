from django.db import models

class Room(models.Model):
    room_code = models.CharField(max_length=255)
    members = models.IntegerField()