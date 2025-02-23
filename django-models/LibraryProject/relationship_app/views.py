from django.shortcuts import render
from django.views.generic.detail import DetailView  # ✅ Explicit import for DetailView
from .models import Book, Library  # ✅ Ensures Library is explicitly imported

def list_books(request):
    """Function-based view to list all books in the database."""
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library, listing all books available."""
    model = Library  # ✅ Specifies the Library model
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

