from django.shortcuts import render,redirect
from .models import Dojo,Ninja
# Create your views here.
def index(request):
    if not "del" in request.session:
        request.session["del"]=""
    context = {
        "all_the_Dojos": Dojo.objects.all(),
        "all_the_Ninjas": Ninja.objects.all()
    }
    for k in context:
        if k==request.session["del"]:
            context.pop(k)

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
def delete_dojo(request):
    m=request.post['{{dojo.name}}']
    request.session["del"]=m
    return redirect('/')
