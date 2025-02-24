from django.shortcuts import render
from django.views.generic.detail import DetailView  # ✅ Explicit import for DetailView
from .models import Book, Library

def list_books(request):
    """Function-based view to list all books in the database."""
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
