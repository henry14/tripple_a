from django.conf import settings
from django.db import models

speciality_choices = (
    (('Accident', 'Accident'),
     ('Stroke', 'Stroke'),
     ('Fire', 'Fire'),
     ('Other', 'Other'))
)


class Facility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


class Practitioner(models.Model):  # Consultant model
    consultant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    facility = models.ForeignKey(Facility, related_name='attached_to', on_delete=models.SET_NULL, null=True)
    highest_qualification = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255, choices=speciality_choices)


