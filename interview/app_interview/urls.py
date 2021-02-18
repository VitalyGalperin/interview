from django.urls import path
from .views import *

urlpatterns = [
    path('', InterviewList.as_view(), name='InterviewList'),
    path('interview', InterviewList.as_view(), name='InterviewList'),
    path('answers', AnswersList.as_view(), name='AnswersList'),
    path('questions', QuestionsList.as_view(), name='QuestionsList'),
]