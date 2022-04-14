from django.db import models
from django.db.models.deletion import CASCADE

class Chat(models.Model):
  # id
  user1 = models.ForeignKey('account.User', on_delete=CASCADE, default='', related_name='user1')
  user2 = models.ForeignKey('account.User', on_delete=CASCADE, default='', related_name='user2')
  last_content = models.CharField(max_length = 200)
  last_time = models.DateTimeField(default = 0)

class Contents(models.Model):
  room= models.ForeignKey('chat.Chat', on_delete=CASCADE, default='', related_name='room')
  writer = models.ForeignKey('account.User', on_delete=CASCADE, default='', related_name='chat')
  time = models.DateTimeField(default=0)
  body = models.CharField(max_length = 200)