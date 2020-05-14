from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('question/<int:id>/', views.question, name='question'),
    path('myquestions/', views.user_questions, name='user_questions'),
    path('myanswers/', views.user_answers, name='user_answers'),
    path('upvote/<int:id>/<str:action>/', views.upvote, name='user_upvote'),
    path('submission/', views.submitq, name='submit'),
    path('search/', views.searchquestions.as_view(), name='search'),
]
