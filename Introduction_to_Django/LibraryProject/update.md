from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=1)
print(updated_book.title)