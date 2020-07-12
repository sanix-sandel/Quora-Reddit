from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, JsonResponse
from quans.models import Question

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (
    QuestionSerializer,
    AnswerSerializer,
    MyUserSerializer,
    ActionSerializer,
    NotificationSerializer,
    GroupeSerializer,
    AnswerActionSerializer
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
def like(request, *args, **kwargs):
    print(request.data)
    serializer=AnswerActionSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        data=serializer.validated_data
        answer_id=data.get("id")
        action=data.get("action")
        answer=Answer.objects.filter(id=answer_id)
        if not answer.exists():
            return Response({}, status=404)
        answer=answer.first()
        if action=="like":
            answer.user_upvote.add(request.user)
            answer.liked+=1
            serializer=AnswerSerializer(answer)
            return Response(serializer.data, status=200)
        else:
            answer.user_upvote.remove(request.user)
            answer.liked-=1
            serializer=AnswerSerializer(answer)
            return Response(serializer.data, status=200)
    return Response({}, status=200)        




@api_view(['POST'])
def ask(request, *args, **kwargs):
    serializer=QuestionSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(submitted_by=request.user)
        return Response(serializer.data, status=201)    
    return Response({}, status=400)                