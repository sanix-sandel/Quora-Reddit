from django.urls import path
from . import views


urlpatterns=[
    path('', views.questions_list),
    path('ask/', views.ask),
    path('questions-list/', views.QuestionList.as_view()),
    path('answers-list/', views.AnswerList.as_view()),
    path('users-list/', views.UserList.as_view()),
]