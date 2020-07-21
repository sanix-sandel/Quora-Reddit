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
    GroupSerializer,
    AnswerActionSerializer, 
    GroupActionSerializer
)

from rest_framework import serializers
from quans.models import Question, Answer
from accounts.models import MyUser
from actions.models import Action
from actions.models import Notification
from groups.models import Groupe

from rest_framework import generics
from actions.utils import create_action


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
        print(action)
        answer=Answer.objects.filter(id=answer_id)
        if not answer.exists():
            return Response({}, status=404)
        answer=answer.first()
        if action=="like":
            answer.user_upvote.add(request.user)
            answer.likes+=1
            answer.save()
            serializer=AnswerSerializer(answer)
            return Response(serializer.data, status=201)
        else:
            answer.user_upvote.remove(request.user)
            answer.likes-=1
            answer.save()
            serializer=AnswerSerializer(answer)
            return Response(serializer.data, status=201)
    return Response({}, status=200)        


@api_view(['POST'])
def add_or_remove(request, *args, **kwargs):
    serializer=GroupActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data=serializer.validated_data
        user_id=data.get("user_id")
        group_id=data.get("id")
        action=data.get("action")
        user=get_object_or_404(MyUser, id=user_id)
        groupe=get_object_or_404(Groupe, id=group_id)
        if action=="accept":
            groupe.member.add(user)
            groupe.save() 
            serializer=GroupSerializer(groupe)
            return Response(serializer.data, status=201)
        else:
            groupe.member.remove(user)
            groupe.save() 
            serializer=GroupSerializer(groupe)
            return Response(serializer.data, status=201)
    return Response({}, status=200) 


@api_view(['POST'])
def join_or_leave(request, *args, **kwargs):
    serializer=GroupActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data=serializer.validated_data
        #user_id=data.get("user_id")
        group_id=data.get("id")
        action=data.get("action")
        user=request.user
        groupe=Groupe.objects.filter(id=group_id) 
        if not groupe.exists():
            return Response({}, status=404)
        groupe=groupe.first()    
        if action=='join':
            if groupe.private:
                create_action(request.user, ' wants to join ', groupe)
                groupe.membersrequested.members.add(request.user)
                
            else:
                 groupe.member.add(user)
            groupe.save()
            serializer=GroupSerializer(groupe)
            return Response(serializer.data, status=201)
        else:
            groupe.member.remove(user)
            groupe.save()
            serializer=GroupSerializer(groupe)
            return Response(serializer.data, status=201)
    return Response({}, status=200)        


@api_view(['POST'])
def remove_member(request, *args, **kwargs):
    serializer=GroupActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data=serializer.validated_data
        id=data.get("id")
        user_id=data.get("user_id")
        groupe=Groupe.objects.filter(id=id)
        user=MyUser.objects.filter(id=user_id)
        if not (groupe.exists() or user.exists()):
            return Response({}, status=404)
        groupe=groupe.first()
        user=user.first()
        groupe.member.remove(user)    
        groupe.save()
        serializer=GroupSerializer(groupe)
        return Response(serializer.data, status=201)
    return Response({}, status=200)    



def RemoveMember(request, id, g_id):
    user=get_object_or_404(MyUser, id=id)
    groupe=get_object_or_404(Groupe, id=id)
    groupe.member.remove(user)
    groupe.save()
    return redirect('groupe_members', id=g_id)


@api_view(['POST'])
def ask(request, *args, **kwargs):
    serializer=QuestionSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(submitted_by=request.user)
        return Response(serializer.data, status=201)    
    return Response({}, status=400)                