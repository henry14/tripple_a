from django.conf.urls import url as path

from services.views import QuestionChoiceListView, QuestionChoiceCreateView, QuestionChoiceDetailView, \
    QuestionChoiceUpdateView, QuestionChoiceDeleteView, index, room

urlpatterns = (

    path(r'^(?P<room_name>\w+)/$', room, name='room'),
    path(r'^question_list/$', QuestionChoiceListView.as_view(), name='question_list'),
    path(r'^question_add/$', QuestionChoiceCreateView.as_view(), name='question_add'),
    path(r'^question_detail/(?P<pk>\d+)/$', QuestionChoiceDetailView.as_view(), name='question_detail'),
    path(r'^question_change/(?P<pk>\d+)/$', QuestionChoiceUpdateView.as_view(), name='question_change'),
    path(r'^question_delete/(?P<pk>\d+)/$', QuestionChoiceDeleteView.as_view(), name='question_delete'),
path(r'', index, name='index'),
)
