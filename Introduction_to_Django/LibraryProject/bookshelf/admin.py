from django.contrib import admin
from .models import Book

# Customize the admin view for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns shown in list view
    search_fields = ('title', 'author')                     # searchable fields
    list_filter = ('publication_year',)                    # filters on the right sidebar

# Register Book with custom admin
admin.site.register(Book, BookAdmin)
