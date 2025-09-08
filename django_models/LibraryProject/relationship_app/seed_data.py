from relationship_app.models import Author, Book, Library, Librarian

# Clear old data
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

# Create author
author = Author.objects.create(name="J.K. Rowling")

# Create books
book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author)
book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author)

# Create library
library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)

# Create librarian
Librarian.objects.create(name="John Doe", library=library)

print("✅ Sample data created successfully!")
