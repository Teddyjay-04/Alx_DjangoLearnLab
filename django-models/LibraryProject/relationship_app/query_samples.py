from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    return author.books.all() if author else []

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    return library.books.all() if library else []

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    return library.librarian if library else None
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    return author.books.all() if author else []

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    return library.books.all() if library else []

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    return library.librarian if library else None
