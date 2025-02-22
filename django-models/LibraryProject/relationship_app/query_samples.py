# query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by {author_name}: {[book.title for book in books]}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}: {[book.title for book in books]}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}")

# Example usage
if __name__ == "__main__":
    query_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")