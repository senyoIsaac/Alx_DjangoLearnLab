from django.urls import path
from . import views
from .views import list_books


urlpatterns = [
    path('books/', list_books, name='list-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path('accounts/login/', views.custom_login, name='login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    path('accounts/register/', views.register, name='register'),
]