from django.db import models
from django.db.models.deletion import CASCADE

class Chat(models.Model):
  # id
  room_id = models.CharField(max_length = 200, default="")  # 채팅방 id는 주문번호_배달자id로 생성된다.
  user1 = models.ForeignKey('account.User', on_delete=CASCADE, default='', related_name='user1')
  user2 = models.ForeignKey('account.User', on_delete=CASCADE, default='', related_name='user2')
  last_content = models.CharField(max_length = 200, default="")
  last_time = models.DateTimeField(auto_now_add=True, blank=True)

class Contents(models.Model):
  room= models.ForeignKey('chat.Chat', on_delete=CASCADE, default='', related_name='room')
  writer = models.ForeignKey('account.User', on_delete=CASCADE, default='', related_name='chat')
  time = models.DateTimeField(auto_now_add=True, blank=True)
  body = models.CharField(max_length = 200, default="")

# class Hat(models.Model):
#   room_id = models.CharField(max_length = 200, default="")  # 채팅방 id는 주문번호_배달자id로 생성된다.
#   user1 = models.ForeignKey('account.User', on_delete=CASCADE, default='', related_name='user1')
#   user2 = models.ForeignKey('account.User', on_delete=CASCADE, default='', related_name='user2')
#   last_content = models.CharField(max_length = 200, default="")
#   last_time = models.DateTimeField(default = 0)