from django.http.response import HttpResponseBadRequest, HttpResponseBase
from django.shortcuts import redirect, render,HttpResponse

def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse('This is placeholder to later display a list of all blogs')
def new(request):
    return HttpResponse('This is placeholder to display a new form to create a new blog')    
def create(request):
    return redirect("/")
def show(request,number):
    return HttpResponse(f'placeholder to display blog number: {number}')
def edit(request,number):
    return HttpResponse(f'placeholder to edit blog: {number}')
def destroy(request):
    return redirect("/blogs")
