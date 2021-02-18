from rest_framework.views import APIView, Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import *
from .serializers import *


class InterviewList(APIView):
    def get(self, request):
        interviews = Interviews.objects.all()
        serializer = InterviewsSerializer(interviews, many=TabError)
        return Response(serializer.data)


class AnswersList(APIView):
    def get(self, request):
        answers = Answers.objects.filter(user_id=self.request.user)
        serializer = AnswersSerializer(answers, many=TabError)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class QuestionsList(APIView):
    def get(self, request):
        questions = Questions.objects.all()
        serializer = QuestionsSerializer(questions, many=TabError)
        return Response(serializer.data)

