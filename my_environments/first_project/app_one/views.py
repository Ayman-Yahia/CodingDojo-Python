from django.http.response import HttpResponseBadRequest
from django.shortcuts import render,HttpRespons

# Create your views here.
def index(request):
    return HttpRespons("this is the equivalent of app.route('/)")