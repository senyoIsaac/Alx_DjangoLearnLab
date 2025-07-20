from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """Helper function to create sample data"""
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")

    # Create books
    book1 = Book.objects.create(title="Harry Potter", author=author1)
    book2 = Book.objects.create(title="A Game of Thrones", author=author2)
    book3 = Book.objects.create(title="The Chamber of Secrets", author=author1)

    # Create library
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2, book3)

    # Create librarian
    librarian = Librarian.objects.create(name="Sarah Johnson", library=library)

def query_all_books_by_author(author):
    """Query all books by a specific author"""
    books = Author.objects.get(author=author)
    print(f"Books by {author}:")
    for book in books:
        print(f"- {book.title}")

def query_all_books_in_library(library_name):
    """List all books in a library"""
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name}:")
    for book in books:
        print(f"- {book.title} (by {book.author.name})")

def query_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library_name}: {librarian.name}")

if __name__ == "__main__":
    # Create sample data first
    create_sample_data()
    
    # Run sample queries
    print("\n1. Query all books by a specific author:")
    query_all_books_by_author("J.K. Rowling")
    
    print("\n2. List all books in a library:")
    query_all_books_in_library("Central Library")
    
    print("\n3. Retrieve the librarian for a library:")
    query_librarian_for_library("Central Library")