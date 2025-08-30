# Delete Operation for Book Model

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion
books = Book.objects.all()
print(books)

# Expected output:
# <QuerySet []>
