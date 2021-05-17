from django.shortcuts import render,redirect
import random

# Create your views here.
def index(request):
    if not 'counter' in request.session:
        request.session['counter']=0
    if "target_number" not in request.session:
        request.session["target_number"] = random.randint(1, 100)
    return render(request,"index.html")
def sub(request):
    if int(request.POST["guess"]) == request.session["target_number"]:
        request.session["submition_result"] = "Correct"
    elif int(request.POST["guess"]) > request.session["target_number"]:
        request.session["submition_result"] = "high"
    else:
        request.session["submition_result"] = "low"
    request.session['counter']+=1
    return redirect("/")
def again(request):
    request.session['counter']=0
    request.session.pop("target_number")
    request.session.pop("submition_result")
    return redirect("/")

