from django.shortcuts import render, redirect, HttpResponse
from time import strftime, localtime
import random, datetime


def index(request):
    if not "Gold" in request.session:
        request.session["Gold"]=0
    if not "activities" in request.session:
        request.session['activities']=[]
    if not "rand" in request.session:
        request.session["rand"]=0
    return render(request, "index.html")
def process(request):
    timestamp = strftime('%#H:%M:%S%p, %B %#d, %Y', localtime())  
    request.session["rand"]=random.randint(0,1)
    if request.POST['location']=='Farm':
        amount_to_add_or_loose=random.randint(10,20)
        # activity=f"Earned {amount_to_add_or_loose} golds from Farm at {timestamp}"
        activity=f"<div class='gain'>Earned {amount_to_add_or_loose} golds from Farm at {timestamp}</div>"
    elif request.POST['location']=='Cave':
        amount_to_add_or_loose=random.randint(5,10)
        # activity=f"Earned {amount_to_add_or_loose} golds from Cave at {timestamp}"
        activity=f"<div class='gain'>Earned {amount_to_add_or_loose} golds from Cave at {timestamp}</div>"
    elif request.POST['location']=='House':
        amount_to_add_or_loose=random.randint(2,5)
        # activity=f"Earned {amount_to_add_or_loose} golds from House at {timestamp}"
        activity=f"<div class='gain'>Earned {amount_to_add_or_loose} golds from House at {timestamp}</div>"
    elif request.POST['location']=='Casino':
        amount_to_add_or_loose=random.randint(-50,50)
        if amount_to_add_or_loose>=0:
            # activity=f"Entered the Casino and earned {amount_to_add_or_loose} golds ...yay...{timestamp}"
            activity=f"<div class='gain'>Entered the Casino and earned {amount_to_add_or_loose} golds ...yay...{timestamp}</div>"
        else:
            # activity=f"<Entered the Casino and lost {-(amount_to_add_or_loose)} golds ...Oush... {timestamp}"
            activity=f"<div class='loss'>Entered the Casino and lost {-(amount_to_add_or_loose)} golds ...Oush... {timestamp}</div>"
    request.session["Gold"]+=amount_to_add_or_loose
    request.session['activities'].append(activity)
    return redirect ('/')
def reset(request):
    request.session.clear()
    return redirect ('/')