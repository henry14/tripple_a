from django.conf.urls import url as path, include
from django.views import generic
from viewflow.flow.viewset import FlowViewSet

from ambulances.flows import EmergencyFlow

# app_name = "Ambulances"

emergency_urls = FlowViewSet(EmergencyFlow).urls

urlpatterns = (
    path(r'^ambulances/', include((emergency_urls, 'emergency'), namespace='emergency')),
    path(r'^$', generic.RedirectView.as_view(url='/workflow/', permanent=False)),

)
