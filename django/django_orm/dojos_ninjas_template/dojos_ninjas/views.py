from django.shortcuts import render,redirect
from .models import Dojo,Ninja
# Create your views here.
def index(request):
    context = {
        "all_the_Dojos": Dojo.objects.all(),
        "all_the_Ninjas": Ninja.objects.all()
    }

    return render(request,'index.html',context)
def add_Dojo(request):
    name=request.POST['name']
    city=request.POST['city']
    state=request.POST['state']
    Dojo.objects.create(
        name=name,
        city=city,
        state=state
    )
    return redirect('/')
def add_Ninja(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    dojo=Dojo.objects.get(name=request.POST['dojo'])
    Ninja.objects.create(
        first_name=first_name,
        last_name=last_name,
        dojo=dojo
    )
    return redirect('/')
def delete_dojo(request,dojo_id):
    m=Dojo.objects.get(id=dojo_id)
    m.delete()
    return redirect('/')
