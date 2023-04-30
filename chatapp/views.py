from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import models
from .forms import ChatRoomForm
from .models import ChatRoom, ChatMessage

@login_required
def create_chat_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            chat_room = form.save(commit=False)
            chat_room.creator = request.user
            chat_room.save()
            chat_room.participants.add(request.user)
            return redirect('chat_room', room_id=chat_room.id)
    else:
        form = ChatRoomForm()
    return render(request, 'chatapp/create_chat_room.html', {'form': form})

@login_required
def chat_room(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    messages = ChatMessage.objects.filter(room=room).order_by('-created_at')[:50]
    return render(request, 'chatapp/chat_room.html', {'room': room, 'messages': messages})

@login_required
def send_message(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    message = request.POST['message']
    ChatMessage.objects.create(room=room, sender=request.user, message=message)
    return redirect('chat_room', room_id=room_id)