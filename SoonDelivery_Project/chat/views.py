from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from delivery.models import delivery_info
from django.db.models import Q
from .models import Chat, Contents

def chat(request, user_id = 0):
  if user_id == 0:
    redirect('login')
  
  rooms = Chat.objects.filter(Q(user1 = User.objects.get(id = user_id)) | Q(user2 = User.objects.get(id = user_id)))  
  return render(request, 'chat/chat-1.html', {
      'user_id': user_id,
      'rooms': rooms
      })

def room(request, room_id):
    try:
      room = get_object_or_404(Chat, id=room_id)
      print(room.room_title)
      return render(request, 'chat/room-1.html', {
        'room': room,
        'room_id':room_id
        })
    except ValueError:
      print("방없음")
      return redirect("home")

def create_room(request):
  if request.method == 'POST':
    chatings = Chat.objects.filter(Q(user1 = User.objects.get(id = request.POST["user1_id"])) & Q(user2 = User.objects.get(id = request.POST["user2_id"])))
    if len(chatings) == 0:
      chatings = Chat.objects.filter(Q(user1 = User.objects.get(id = request.POST["user2_id"])) & Q(user2 = User.objects.get(id = request.POST["user1_id"])))
      if len(chatings) == 0:
        new_room = Chat()
        new_room.user1 = User.objects.get(id = request.POST["user1_id"]) # 배달자(본인)
        new_room.user2 = User.objects.get(id = request.POST["user2_id"]) # 주문자
        new_room.room_title = str(new_room.user1.nickname) + ", " + str(new_room.user2.nickname) + "의 채팅방" # 방 제목
        new_room.save()
        return redirect('start_delivery', room_id=new_room.id, user_id=request.POST["user1_id"], order_id=request.POST["order_id"])

      else: #채팅방이 있는 경우 2
        return redirect('start_delivery', room_id=chatings[0].id,  user_id=request.POST["user1_id"], order_id=request.POST["order_id"])

    else: # 채팅방이 있는 경우 1
      return redirect('start_delivery',  room_id=chatings[0].id, user_id=request.POST["user1_id"], order_id=request.POST["order_id"])

  else:
    return render(request, 'delivery.html')