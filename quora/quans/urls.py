from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('question/<int:id>/', views.question, name='question'),
    path('submission/', views.submitq, name='submit'),
]