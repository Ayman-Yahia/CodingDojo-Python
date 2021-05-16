from django.shortcuts import redirect, render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def result(request):
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    loc = request.POST['location']
    lang = request.POST['language']
    comm = request.POST['comments']
    context = {
    	"first_name" : fname,
    	"last_name" : lname,
        "location" :loc,
        "language" :lang,
        "comments" :comm
    }
    return render(request,"result.html",context)
