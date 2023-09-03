from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    content= models.CharField(max_length=2048)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message by {self.user} at {self.time.strftime("%m/%d/%Y, %H:%M:%S")}'
