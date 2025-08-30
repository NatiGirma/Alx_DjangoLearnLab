# Retrieve Operation for Book Model

```python
from bookshelf.models import Book

# Retrieve all Book instances
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)

# Expected output:
# 1984 George Orwell 1949

