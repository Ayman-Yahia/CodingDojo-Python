from django.shortcuts import render,redirect
from .models import  Book,Author
# Create your views here.
def index(request):
    if not "title_book" in request.session:
        request.session["title_book"]=''
    if not "title_desc" in request.session:
        request.session["title_desc"]='' 
    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all()
    }
    return render(request,'index.html',context)
    
def add_book(request):
    title=request.POST['title']
    desc=request.POST['desc']
    request.session["title_book"]=title
    request.session["title_desc"]=desc
    Book.objects.create(
        title=title,
        desc=desc
    )
    return redirect('/')
def book_desc(request,book_id):
    if not "b_id" in request.session:
        request.session['b_id']=book_id
    b=Book.objects.get(id = book_id)
    r=b.authors.all()
    context1 = {
        'books' : Book.objects.get(id=book_id),
        'all_the_authors' : Author.objects.exclude(first_name=),
        'authors':b.authors.all()
    }
    return render(request,'book.html',context1)
def add_author_to_book(request):
    c=request.session['b_id']
    option = Author.objects.get(id=request.POST['select_author'])
    a=Book.objects.get(id = c)
    a.authors.add(option)
    return redirect(f'/books/{c}')
def index1(request):
    if not "author_first" in request.session:
        request.session["author_first"]=''
    if not "author_last" in request.session:
        request.session["author_last"]=''
    if not "author_notes" in request.session:
        request.session["author_notes"]=''
    context2 = {
        "all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all()
    }
    return render(request,'index1.html',context2)
def add_author(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    notes=request.POST['notes']
    request.session["author_first"]=first_name
    request.session["author_last"]=last_name
    request.session["notes"]=notes
    Author.objects.create(
        first_name=first_name,
        last_name=last_name,
        notes=notes
    )
    return redirect('/authors')
def author_desc(request,author_id):
    if not "a_id" in request.session:
        request.session['author']=author_id
    m=request.session['author']
    l=Author.objects.get(id=author_id)
    context3 = {
        'author' : Author.objects.get(id=author_id),
        "book_m":l.books.all(),
        "all_the_books":Book.objects.all()
    }
    return render(request,'author.html',context3)
def add_book_to_author(request):
    s=request.session['author']
    option = Book.objects.get(id=request.POST['select_book'])
    a=Author.objects.get(id = s)
    a.books.add(option)
    return redirect(f'/authors/{s}')