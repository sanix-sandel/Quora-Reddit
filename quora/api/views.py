from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, JsonResponse
from quans.models import Question
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def questions_list(request):
    qs=Question.objects.all()
    serializer=QuestionSerializer(qs, many=True)
    return Response(serializer.data, status=200)


          