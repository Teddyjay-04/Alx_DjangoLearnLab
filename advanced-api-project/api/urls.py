
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

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
