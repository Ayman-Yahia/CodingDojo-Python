from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.

    
def time_app(request):
    context = {
        "time": strftime("%H:%M %p", gmtime()),
        "date": strftime("%b %d, %Y", gmtime())
    }
    return render(request, "index.html", context)