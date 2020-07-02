from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, JsonResponse
from quans.models import Question
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (
    QuestionSerializer,
    AnswerSerializer,
    MyUserSerializer,
    ActionSerializer,
    NotificationSerializer,
    GroupeSerializer
)

from rest_framework import serializers
from quans.models import Question, Answer
from accounts.models import MyUser
from actions.models import Action
from actions.models import Notification
from groups.models import Groupe

from rest_framework import generics



class QuestionList(generics.ListAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    

class AnswerList(generics.ListAPIView):
    queryset=Answer.objects.all()
    serializer_class=AnswerSerializer

class UserList(generics.ListAPIView):
    queryset=MyUser.objects.all()
    serializer_class=MyUserSerializer 




@api_view(['GET'])
def questions_list(request):
    qs=Question.objects.all()
    serializer=QuestionSerializer(qs, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def like(request):
    answer=get_object_or_404(Answer, id=id)
    if request.user in answer.user_upvote.all():
        answer.user_upvote.remove(request.user)
    else:
        answer.user_upvote.add(request.user)
        user1=answer.submitted_by


@api_view(['POST'])
def ask(request, *args, **kwargs):
    serializer=QuestionSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(submitted_by=request.user)
        return Response(serializer.data, status=201)    
    return Response({}, status=400)                