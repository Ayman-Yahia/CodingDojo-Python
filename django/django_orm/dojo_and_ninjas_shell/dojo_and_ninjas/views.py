from django.shortcuts import render,redirect
from .models import Dojo,Ninja
# Create your views here.
def index(request):
    return redirect('/')
