from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from delivery.models import delivery_info
from django.db.models import Q
from .models import Chat, Contents

def chat(request, user_id = 0):
  if user_id == 0:
    redirect('login')
  
  rooms = Chat.objects.filter(user1 = User.objects.get(id = user_id))
  return render(request, 'chat/chat.html', {
      'user_id': user_id,
      'rooms': rooms
    })

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def create_room(request):
  if request.method == 'POST':
    chatings = Chat.objects.filter(Q(user1 = User.objects.get(id = request.POST["user1_id"])) & Q(user2 = User.objects.get(id = request.POST["user2_id"])))
    if len(chatings) == 0:
      print("1")
      chatings = Chat.objects.filter(Q(user1 = User.objects.get(id = request.POST["user2_id"])) & Q(user2 = User.objects.get(id = request.POST["user1_id"])))
      if len(chatings) == 0:
        print("2에서 걸림")
        new_room = Chat()
        new_room.user1 = User.objects.get(id = request.POST["user1_id"]) # 배달자(본인)
        new_room.user2 = User.objects.get(id = request.POST["user2_id"]) # 주문자
        new_room.save()

        return redirect('start_delivery', room_id=new_room.id, user_id=request.POST["user1_id"], order_id=request.POST["order_id"])
      else: #채팅방이 있는 경우 2
        print("3에서 걸림")
        return redirect('start_delivery', room_id=chatings[0].id,  user_id=request.POST["user1_id"], order_id=request.POST["order_id"])

    else: # 채팅방이 있는 경우 1
      print("4에서 걸림")
      return redirect('start_delivery',  room_id=chatings[0].id, user_id=request.POST["user1_id"], order_id=request.POST["order_id"])

  else:
    return render(request, 'delivery.html')