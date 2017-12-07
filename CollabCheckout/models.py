from django.db import models

# Create your models here.



class RoomSlot(models.Model):
    period = models.IntegerField()
    checkout_email = models.EmailField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    room = models.CharField(max_length=256)
    reserved = models.BooleanField()
    day_type = models.CharField(max_length=256)

    def __unicode__(self):
        return str(self.period) + " "+ str(self.date) + " " + str(self.room) + " " + str(self.reserved) + ' ' + str(self.day_type)
