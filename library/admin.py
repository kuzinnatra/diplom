from django.contrib import admin
from library.models import Author, Books
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'availability', 'author', 'genre')
    list_filter = ('name', 'availability', 'author', 'genre')
    search_fields = ('name', 'availability', 'author', 'genre')
