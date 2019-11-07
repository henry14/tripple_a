from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.urls import reverse
from django.views.generic import FormView, ListView
from material.frontend.views import ListModelView, CreateModelView, DetailModelView, UpdateModelView, DeleteModelView
from viewflow.flow.views import CreateProcessView, FlowMixin

from ambulances.forms import AcceptAssignmentProcessForm, EmergencyAssessmentForm
from ambulances.models import EmergencyAssessment, Provider
from services.models import Question
from .forms import EmergencyProcessForm


class NearbyProvider(ListModelView):
    user_location = Point(0, 0, srid=4326)
    model = Provider
    context_object_name = 'providers'
    queryset = Provider.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:6]
    # template_name = 'ambulances/providers.html'


class EmergencyProcessView(LoginRequiredMixin, CreateProcessView):
    # template_name = "ambulances/emergency_process_form.html"
    form_class = EmergencyProcessForm


def is_accepted(data):
    for key, value in data.items():
        if key not in ['contact', 'short_notes']:
            if Question.objects.get(question_text=key).preferred_choice is not value:
                return False
    return True


class EmergencyAssessmentView(LoginRequiredMixin, FlowMixin, FormView):
    model = EmergencyAssessment
    form_class = EmergencyAssessmentForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['nature_of_emergency'] = self.activation.process.nature_of_emergency
        return kwargs

    def form_valid(self, form):
        self.activation.process.accept = is_accepted(form.cleaned_data)
        self.activation.process.save()
        self.activation.done()

    def has_object_permission(self, request, obj):
        pass


class DriverAssignmentProcessView(LoginRequiredMixin, CreateProcessView):
    template_name = "ambulances/driver_assignment_form.htm;"
    form_class = AcceptAssignmentProcessForm

