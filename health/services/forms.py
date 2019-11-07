from material import Layout, Span2, Row, Span4
from material.forms import ModelForm, InlineFormSetField

from services.models import Choice, ServiceProvider, Question


class ServiceProviderForm(ModelForm):

    class Meta:
        model = ServiceProvider
        fields = ['code', 'name']


class ChoiceForm(ModelForm):

    class Meta:
        model = Choice
        fields = ['question', 'choice_text']

    layout = Layout(
        Row(Span4('choice_text'))
    )


class QuestionForm(ModelForm):

    choices = InlineFormSetField(
        parent_model=Question,
        model=Choice,
        fields=['choice_text'],
        extra=2
    )

    class Meta:
        model = Question
        fields = ['question_text', 'nature_of_emergency', 'preferred_choice']

    layout = Layout(
        Row(Span2('question_text')),
        Row(Span2('preferred_choice')),
        Row(Span2('nature_of_emergency')),
        Row(Span4('choices'))
    )
