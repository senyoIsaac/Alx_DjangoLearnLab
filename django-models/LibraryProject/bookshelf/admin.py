from django.contrib import admin
from .models import Book
# Register your models here.

admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable filtering by publication year and author
    list_filter = ('publication_year', 'author')
    
    # Add search functionality for title and author
    search_fields = ('title', 'author')
    
    # Set default ordering
    ordering = ('title',)