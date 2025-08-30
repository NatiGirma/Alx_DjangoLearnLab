# Create Operation for Book Model

```python
from bookshelf.models import Book

# Create a new Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
# Expected output: Book instance created successfully and saved to database

