from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views  # Import views from the current app

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
]

