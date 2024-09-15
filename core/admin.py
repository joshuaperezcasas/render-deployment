# admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'pages')
    search_fields = ('title', 'author')
    list_filter = ('published_date',)
    fields = ('title', 'author', 'published_date', 'isbn', 'pages')

admin.site.register(Book, BookAdmin)