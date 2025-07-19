In [1]: from bookshelf.models import Book

In [2]: book = Book.objects.create(title="1984",
   ...: author="George Orwell", publication_year=
   ...: 1949)

In [3]: print(book)
Book object (1)

In [4]: book
Out[4]: <Book: Book object (1)>

In [5]: book = Book.objects.get(id=1)

In [6]: print(book)
Book object (1)

In [7]: book.title
Out[7]: '1984'

In [8]: book.author
Out[8]: 'George Orwell'

In [9]: book.title = "Nineteen Eighty-Four"

In [10]: book.save()

In [11]: updated_book = Book.objects.get(id=1)

In [12]: updated_book.title
Out[12]: 'Nineteen Eighty-Four'

In [13]: book. delete
Out[13]: <bound method Model.delete of <Book: Book object (1)>>

In [14]: book.delete()
Out[14]: (1, {'bookshelf.Book': 1})

In [15]: Book.objects.all()
Out[15]: <QuerySet []>