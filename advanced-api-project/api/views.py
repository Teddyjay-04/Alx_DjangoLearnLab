from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """View to list all books and create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    """View to retrieve a specific book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """View to create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for creating a book

class BookUpdateView(generics.UpdateAPIView):
    """View to update a specific book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for updating a book

class BookDeleteView(generics.DestroyAPIView):
    """View to delete a specific book."""
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for deleting a book