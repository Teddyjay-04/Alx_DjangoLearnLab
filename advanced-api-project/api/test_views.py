from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        """Set up test data for the API tests."""
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", author=self.author, publication_year=2022)

        self.client.login(username="testuser", password="testpassword")

        self.book_list_url = reverse("book-list")  # Ensure your API views have named routes
        self.book_detail_url = reverse("book-detail", args=[self.book.id])

    def test_list_books(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", response.data[0]["title"])

    def test_create_book(self):
        """Test creating a new book."""
        data = {"title": "New Book", "author": self.author.id, "publication_year": 2024}
        response = self.client.post(self.book_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_book(self):
        """Test retrieving a single book."""
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_update_book(self):
        """Test updating a book's details."""
        data = {"title": "Updated Book", "author": self.author.id, "publication_year": 2023}
        response = self.client.put(self.book_detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """Test filtering books by title."""
        response = self.client.get(f"{self.book_list_url}?title=Test Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_search_books(self):
        """Test searching for books using query parameters."""
        response = self.client.get(f"{self.book_list_url}?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books by publication year."""
        Book.objects.create(title="Older Book", author=self.author, publication_year=2000)
        response = self.client.get(f"{self.book_list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Older Book")  # Oldest book should be first
