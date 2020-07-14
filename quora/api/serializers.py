from rest_framework import serializers
from quans.models import Question, Answer
from accounts.models import MyUser
from actions.models import Action
from actions.models import Notification
from groups.models import Groupe

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=(
            'id',
            'username',
            'profile_image',
            'email',
            'about',

        )

class QuestionSerializer(serializers.ModelSerializer):
    submitted_by=MyUserSerializer()
    class Meta:
        model=Question
        fields='__all__'


class AnswerSerializer(serializers.ModelSerializer):
    submitted_by=MyUserSerializer()
    reply_to=QuestionSerializer()
    class Meta:
        model=Answer
        fields='__all__'

class AnswerActionSerializer(serializers.Serializer):
    id=serializers.IntegerField()    
    action=serializers.CharField()

class UserActionSerializer(serializers.Serializer):
    id=serializers.IntegerField()    
    action=serializers.CharField()    

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Action
        fields=(
            '',
        ) 

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=(
            '',
        )               

class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Groupe
        fields=(
            'title',
            'description'
        )        