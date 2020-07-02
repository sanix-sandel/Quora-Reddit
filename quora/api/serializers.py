from rest_framework import serializers
from quans.models import Question, Answer
from accounts.models import MyUser
from actions.models import Action
from actions.models import Notification
from groups.models import Groupe



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=('title', 'body')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=('body',)

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=(
            'id',
            'username',
            'email',
            'about',

        )

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