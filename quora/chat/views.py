from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def chat_room(request):
    return render(request, 'chat/room.html')
