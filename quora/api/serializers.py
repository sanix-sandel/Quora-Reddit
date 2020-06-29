from rest_framework import serializers
from quans.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=('title', 'body')