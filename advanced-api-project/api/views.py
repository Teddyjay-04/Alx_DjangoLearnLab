from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """View to list all books. Accessible to everyone."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read access for all users

class BookDetailView(generics.RetrieveAPIView):
    """View to retrieve a single book by ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """View to add a new book. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can create books

class BookUpdateView(generics.UpdateAPIView):
    """View to update an existing book. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """View to delete a book. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
class BookCreateView(generics.CreateAPIView):
    """View to add a new book with extra validation."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Ensure the book author is provided and valid."""
        if not serializer.validated_data.get('author'):
            raise serializers.ValidationError("Author field is required.")
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """View to update an existing book with validation."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """Ensure title and publication year remain valid."""
        if 'title' in serializer.validated_data and serializer.validated_data['title'].strip() == "":
            raise serializers.ValidationError("Title cannot be empty.")
        serializer.save()
