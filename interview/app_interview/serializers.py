from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import *


class InterviewsSerializer(ModelSerializer):
    class Meta:
        model = Interviews
        fields = ('id', 'title', 'start_at', 'finish_at')


class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = ('id', 'Interview', 'answer_type', 'text')


class OptionsSerializer(ModelSerializer):
    class Meta:
        model = Options
        fields = ('id', 'text', 'question')


class AnswersSerializer(ModelSerializer):
    class Meta:
        model = Answers
        fields = ('id', 'user', 'question', 'text_answer', 'choice_answer')
