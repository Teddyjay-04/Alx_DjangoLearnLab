from django.urls import path
from .views import list_books, LibraryDetailView
from .views import user_login, user_logout, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("books/", list_books, name="list_books"),  # Function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
]
