from django.db import models
from django.shortcuts import redirect, render
from .models import Message,Comment
from ..login_register.models import User

# Create your views here.
def index(request):
    context = {
        'posts':Message.objects.all(),
        'comments':Comment.objects.all()
    }
    return render(request,'index1.html',context)
def add_message(request):
    Message.objects.create(message=request.POST['add_message'], messager=User.objects.get(id=request.session['user_id']))
    return redirect('/wall')
def add_comment(request):
    Comment.objects.create(comment=request.POST['add_comment'],commentor=User.objects.get(id=request.session['user_id']),message_post=Message.objects.get(id=request.POST['comment1']) )
    return redirect('/wall') 
def deletemsg(request, msg_id):
    models.delete_msg(msg_id)
    return redirect('/wall')

def deletecom(request, com_id):
    models.delete_com(com_id)
    return redirect('/wall')
    
def logout(request):
    request.session.flush()
    return redirect('/')
