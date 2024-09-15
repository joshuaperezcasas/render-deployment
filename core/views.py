# views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Retrieve all book records
    return render(request, 'book_list.html', {'books': books})