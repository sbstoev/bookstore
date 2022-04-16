from django.contrib import admin

from bookstore.accounts.models import Profile, BookstoreUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(BookstoreUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
