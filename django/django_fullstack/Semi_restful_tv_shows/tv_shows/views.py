from django.shortcuts import render,redirect
from .models import Show
from datetime import datetime, time, timezone
from time import gmtime, strftime
# Create your views here.
def index(request):
    return redirect('/shows')
def index1(request):
    context={
        "all_the_shows":Show.objects.all()
    }
    return render (request,'index.html',context)
def show_create(request):
    show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['description'])
    return redirect(f"/shows/{show.id}")
def new_show(request):
    return render(request,"create.html")
def show(request,show_id):
    context1={
        "shows":Show.objects.get(id=show_id)
    }
    return render(request,"show.html",context1)
def edit(request,show_id):
    if not "s_id" in request.session:
        request.session["s_id"]=0
    return render(request,"edit.html")
def show_edit(request,show_id):
    context2={
        "shows":Show.objects.get(id=show_id)
    }
    return render(request,"edit.html",context2)
def show_update(request,show_id):
    m=Show.objects.get(id=show_id)
    m.update_show(request.POST['title'],request.POST['network'],request.POST['release_date'],request.POST['description'])
    return redirect(f'/shows/{show_id}')
def destroy(request,show_id):
    s=Show.objects.get(id=show_id)
    s.delete_show(show_id)
    return redirect('/shows')