from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views from the current app
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
    path('books/', include('relationship_app.urls')),

]