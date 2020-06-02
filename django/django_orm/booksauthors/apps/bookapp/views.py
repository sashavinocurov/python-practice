from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    context={
        "allbooks": Book.objects.all(),
    }
    return render(request, "bookapp/index.html",context)

def displaybook(request, x,):
    Book.objects.get(id=x)
    context= {
        "allbooks1": Book.objects.get(id=x),
        "authorinbook": Book.objects.get(id=x).authors.all(),
        "authorsall": Author.objects.all(),
        "bookid": x,
    }
    return render(request, "bookapp/bookdisplay.html",context)

def processauthor(request, x):
    Book.objects.get(id=x).authors.add(Author.objects.get(id=request.POST['author']))
    return redirect(f"/{x}")

def authors(request):
    context={
        "allauthors":Author.objects.all(),
    }
    return render(request, "bookapp/author.html",context)

def displayauthor(request, y):
    Author.objects.get(id=y)
    context={
        "allauthors1":Author.objects.get(id=y),
        "bookinauthor": Author.objects.get(id=y).books.all(),
        "booksall": Book.objects.all(),
        "authorid": y,
    }
    return render(request, "bookapp/authordisplay.html", context)

def processbook(request,y):
    Author.objects.get(id=y).books.add(Book.objects.get(id=request.POST['book']))
    return redirect(f"/authors/{y}")

def addbook(request):
    Book.objects.create(title=request.POST['title'], description=request.POST['description'])
    return redirect("/")

def addauthor(request):
    Author.objects.create(first_name= request.POST['first_name'], last_name= request.POST['last_name'], notes= request.POST['notes'])
    return redirect("/authors")

