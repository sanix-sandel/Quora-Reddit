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
            'is_superuser',
            'username',
            'email',
            'date_of_birth',
            'profile_image',
            'about',
            'is_active',
            'is_admin',
            'groups',
            'following',
            'questions_submitted'
        )

class QuestionSerializer(serializers.ModelSerializer):
    submitted_by=MyUserSerializer()
    class Meta:
        model=Question
        fields='__all__'

class QuestionGroupSerializer(serializers.ModelSerializer):
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





class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Action
        fields='__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields='__all__'     


class GroupSerializer(serializers.ModelSerializer):
    owner=MyUserSerializer()
    #member=MyUserSerializer(many=True, read_only=True)
    questions=QuestionSerializer(many=True, read_only=True)
    #questions=serializers.StringRelatedField(source='question.title')
    class Meta:
        model=Groupe
        fields=('__all__')


class GroupActionSerializer(serializers.Serializer):
    id=serializers.IntegerField()    
    action=serializers.CharField()    
    user_id=serializers.IntegerField()    