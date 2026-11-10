from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})


def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def viewbook(request, bookId):
    book1 = {
        'id': 123,
        'title': 'Continuous Delivery',
        'author': 'J. Humble and D. Farley'
    }
    book2 = {
        'id': 456,
        'title': 'Secrets of Reverse Engineering',
        'author': 'E. Eilam'
    }
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2
    return render(request, 'bookmodule/show.html', {'book': targetBook})


def one_book(request):
    return render(request, "bookmodule/one_book.html")


def html5_links(request):
    return render(request, "bookmodule/links.html")


def html5_formatting(request):
    return render(request, "bookmodule/formatting.html")


def html5_listing(request):
    return render(request, "bookmodule/listing.html")


def html5_tables(request):
    return render(request, "bookmodule/tables.html")
