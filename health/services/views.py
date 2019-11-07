import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.utils.safestring import mark_safe
from material.frontend.views import ListModelView, CreateModelView, DetailModelView, UpdateModelView, DeleteModelView

from services.forms import QuestionForm
from services.models import Question


class QuestionChoiceListView(ListModelView):
    template_name = "services/questions_list.html"
    model = Question
    list_display = ('question_text', 'nature_of_emergency', 'preferred_choice')
    queryset = Question.objects.all()


class QuestionChoiceCreateView(LoginRequiredMixin, CreateModelView):
    template_name = "services/question_add.html"
    model = Question
    queryset = Question.objects.all()
    form_class = QuestionForm

    def has_object_permission(self, request, obj):
        pass


class QuestionChoiceDetailView(LoginRequiredMixin, DetailModelView):
    template_name = "services/question_detail.html"
    model = Question


class QuestionChoiceUpdateView(LoginRequiredMixin, UpdateModelView):
    template_name = "services/question_update.html"
    form_class = QuestionForm
    model = Question

    def get_success_url(self):
        return reverse('services:question_list')


class QuestionChoiceDeleteView(LoginRequiredMixin, DeleteModelView):
    template_name = "services/confirm_delete.html"
    model = Question

    def get_success_url(self):
        return reverse('services:question_list')


def index(request):
    return render(request, 'services/index.html', {})


def room(request, room_name):
    return render(request, 'services/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
