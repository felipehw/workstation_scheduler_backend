from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Workstation(models.Model):
    WORKSTATION_AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('scheduled', 'Scheduled'),
    ]

    workstation_id = models.AutoField(primary_key=True)
    workstation_name = models.CharField(max_length=255)
    availability_status = models.CharField(
        max_length=255,
        choices=WORKSTATION_AVAILABILITY_CHOICES,
        default='available'
    )


class Schedule(models.Model):
    SCHEDULE_TIME_SLOT_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('night', "Night")
    ]

    schedule_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    workstation = models.ForeignKey(Workstation, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    time_slot = models.CharField(
        max_length=255,
        choices=SCHEDULE_TIME_SLOT_CHOICES
    )
