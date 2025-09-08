from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)
print("Books by J.K. Rowling:", [book.title for book in books_by_author])

# Query 2: List all books in a specific library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("Books in Central Library:", [book.title for book in books_in_library])

# Query 3: Retrieve the librarian for a library
librarian = library.librarian
print("Librarian of Central Library:", librarian.name)
