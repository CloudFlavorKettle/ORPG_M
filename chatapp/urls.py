from django.urls import path
from . import views

app_name = 'chatapp'

urlpatterns = [
    path('<int:room_id>/', views.chat_room, name='chat_room'),
    path('<int:room_id>/send/', views.send_message, name='send_message'),
    path('create_chat_room/', views.create_chat_room, name='create_chat_room'),
]
