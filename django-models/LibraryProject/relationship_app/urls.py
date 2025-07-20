from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books


urlpatterns = [
    path('books/', list_books, name='list-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
   path('accounts/login/', 
         auth_views.LoginView.as_view(template_name='registration/login.html'), 
         name='login'),
    path('accounts/logout/', 
         auth_views.LogoutView.as_view(template_name='registration/logout.html'), 
         name='logout'),
    
    # Registration URL
    path('accounts/register/', views.register, name='register'),
    path('admin-dashboard/', views.admin_view, name='admin-view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian-view'),
    path('member-dashboard/', views.member_view, name='member-view'),
]