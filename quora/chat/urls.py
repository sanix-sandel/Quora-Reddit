
from django.urls import path, include
from . import views


urlpatterns = [

    path('room/', views.chat_room, name='chat_room'),


]
