import json

from django.conf import settings
from django.contrib.gis.db.models import PointField
from django.contrib.postgres.fields import JSONField
from django.db import models
from viewflow.models import Process, Subprocess

nature_of_emergency_choices = (
    (('Accident', 'Accident'),
     ('Stroke', 'Stroke'),
     ('Fire', 'Fire'),
     ('Other', 'Other'))
)


class Provider(models.Model):
    name = models.CharField(max_length=100)
    location = PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EmergencyProcess(Process):
    point = PointField(null=True)
    nature_of_emergency = models.CharField(choices=nature_of_emergency_choices, max_length=255)
    question_answer = JSONField(null=True)  # Stores each question-answer pair, service provider
    accept = models.BooleanField(default=False)


class EmergencyAssessment(models.Model):
    emergency_process = models.OneToOneField(EmergencyProcess, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    contact = models.CharField('At least two cell phone contacts separated by commas', max_length=255, default='')
    location = models.CharField(max_length=255)
    short_notes = models.CharField(max_length=500)


class DriverAssignmentProcess(Subprocess):
    emergency_process = models.OneToOneField(EmergencyProcess, on_delete=models.CASCADE)
    driver = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rejecting_drivers = JSONField(null=True)  # Keep record of drivers rejecting jobs for quality purposes

