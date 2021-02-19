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
    def get(self, request, user_id):
        if request.user.is_authenticated and request.user.id == user_id:
            user_id = self.request.user
            answers = Answers.objects.filter(user_id=user_id)
        else:
            answers = Answers.objects.filter(anon_user=user_id)
        serializer = AnswersSerializer(answers, many=TabError)
        return Response(serializer.data)

    def post(self, request, user_id):
        if request.user.is_authenticated and request.user.id == user_id:
            request.data['anon_user'] = None
            request.data['user'] = user_id
        else:
            request.data['anon_user'] = user_id
            request.data['user'] = None
        serializer = AnswersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class QuestionsList(APIView):
    def get(self, request, interview_id):
        questions = Questions.objects.filter(Interview=interview_id)
        serializer = QuestionsSerializer(questions, many=TabError)
        return Response(serializer.data)

