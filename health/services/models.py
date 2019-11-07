from django.conf import settings
from django.db import models


nature_of_emergency_choices = (
    (('Accident', 'Accident'),
     ('Stroke', 'Stroke'),
     ('Fire', 'Fire'),
     ('Other', 'Other'))
)


class ServiceProvider(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField('Created date', auto_now_add=True, )
    last_modified = models.DateTimeField('Last modified date', auto_now=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    """ The questions should be generic, this allows competition thrive.
    Could decide to make it service provider specific if a  strong argument for this arises.
    Given these are emergencies, could allow the client to always opt for a given service provider,
    hence service provider specific questions if any.
    These could be additions to the generic ones """
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=255, unique=True)
    nature_of_emergency = models.CharField(choices=nature_of_emergency_choices, max_length=255)
    preferred_choice = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField('Created date', auto_now_add=True, )
    last_modified = models.DateTimeField('Last modified date', auto_now=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField('Created date', auto_now_add=True, )
    last_modified = models.DateTimeField('Last modified date', auto_now=True)
