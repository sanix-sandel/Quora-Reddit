from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    
    path('question/<int:id>/', views.question, name='question'),
    path('myquestions/', views.user_questions.as_view(), name='user_questions'),
    path('myanswers/', views.user_answers, name='user_answers'),
    path('upvote/<int:id>/<str:action>/', views.upvote, name='user_upvote'),
    path('submission/', views.submitq, name='submit'),
    path('editans/<int:pk>', views.edita.as_view(), name='edit_ans'),
    path('editq/<int:pk>', views.editq.as_view(), name='editq'),
    path('deleteq/<int:pk>', views.deleteq.as_view(), name='deleteq'),
   # path('reply/<int:a_id>/<int:q_id>/', views.Reply, name='reply'),
    #path('search/', views.searchquestions.as_view(), name='search'),

]
