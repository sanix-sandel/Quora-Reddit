from django.urls import path
from .import consumers
from channels.auth import AuthMiddlewareStack


websocket_urlpatterns=[
    path('ws/api', consumers.ApiConsumer)
]