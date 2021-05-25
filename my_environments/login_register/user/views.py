from django.db.models.fields import EmailField
from django.shortcuts import redirect, render,HttpResponse
from .models import User

# Create your views here.
def index(request):
    return render (request,"index.html")
def add_new_user(request):
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'])
    return redirect ('/')
def login_user(request):
    user_password=request.POST['c_password']
    if User.objects.get(email=request.POST['c_email']).password == user_password:
        context={ 
            "user":User.objects.get(email=request.POST['c_email']),
            "m":'You logged in succesfully'
        }  
    else:
        context={
            "m":'The information you provided is wrong'
        }      

    
    return render(request,'user.html',context)