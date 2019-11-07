from django import forms
from material import Layout, Span4, Row, Span2
from material.forms import ModelForm, InlineFormSetField, ForeignKeyFormField, Form

from ambulances.models import EmergencyProcess, EmergencyAssessment
from services.models import Question, Choice


class EmergencyProcessForm(ModelForm):

    class Meta:
        model = EmergencyProcess
        fields = ['nature_of_emergency']


class EmergencyAssessmentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        nature_of_emergency = kwargs['nature_of_emergency']
        super(EmergencyAssessmentForm, self).__init__()
        for question in Question.objects.filter(nature_of_emergency__iexact=nature_of_emergency):
            self.fields['%s' % question] = forms.ModelChoiceField(queryset=Choice.objects.filter(question=question))

    class Meta:
        model = EmergencyAssessment
        fields = ['contact', 'short_notes']


class AcceptAssignmentProcessForm(Form):
    accept = forms.BooleanField(required=True)
