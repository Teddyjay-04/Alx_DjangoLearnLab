from django.urls import path
from .views import list_books, LibraryDetailView
from .views import user_login, user_logout, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
]
