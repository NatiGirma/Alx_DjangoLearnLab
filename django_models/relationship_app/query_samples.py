import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# -----------------------------
# Sample Queries
# -----------------------------

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        return author.books.all()
    return []

# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.books.all()
    return []

# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library and hasattr(library, 'librarian'):
        return library.librarian
    return None

# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("Books by Author 'Alice':", books_by_author('Alice'))
    print("Books in Library 'Central Library':", books_in_library('Central Library'))
    print("Librarian for 'Central Library':", librarian_for_library('Central Library'))
