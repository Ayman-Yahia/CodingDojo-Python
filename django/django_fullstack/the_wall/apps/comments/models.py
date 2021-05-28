from django.db import models
from ..login_register.models import User

# Create your models here.
class Message(models.Model):
    message = models.TextField(null=True)
    messager= models.ForeignKey(User, related_name="messages_made",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def delete_msg(self,msg_id):
        msg=Message.objects.get(id=msg_id)
        msg.delete()

class Comment(models.Model):
    comment = models.TextField(null=True)
    commentor = models.ForeignKey(User, related_name="comments_made",on_delete=models.CASCADE)
    message_post = models.ForeignKey(Message, related_name="post_comment",null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def delete_msg(self,com_id):
        com=Message.objects.get(id=com_id)
        com.delete()