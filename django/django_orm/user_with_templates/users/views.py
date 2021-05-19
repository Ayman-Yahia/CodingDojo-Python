from django.shortcuts import redirect, render,HttpResponse
from .models import User

# Create your views here.
def index(request):
    context = {
        "all_the_users": User.objects.all()
    }
    return render(request,"index.html",context)
def add_users_to_the_table(requset):
    first_name=requset.POST['first_name']
    last_name=requset.POST['last_name']
    email=requset.POST['email']
    age=requset.POST['age']
    User.objects.create(
        firstname=first_name,
        lastname=last_name,
        email=email,
        age=age
    )
    return redirect ('/')