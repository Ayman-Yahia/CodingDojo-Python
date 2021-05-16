import counter
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if not 'counter' in request.session:
        request.session['counter']=1
    request.session['counter']+=1
    return render(request,"index.html")

def add(request):
    request.session['counter'] += 1
    return redirect("/")
    
def destroy(request):
    request.session['counter'] = 0
    return redirect("/")

