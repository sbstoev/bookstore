from django.contrib import admin

from bookstore.main.models import Book, Author, Event


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'country', 'date')
