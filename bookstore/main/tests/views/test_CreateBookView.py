
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from bookstore.accounts.models import Profile
from bookstore.accounts.tests.views.test_ProfileDetailsView import UserModel
from bookstore.main.models import Book


class CreateBookViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'testuser',
        'password': '12345qwe',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Doncho',
        'last_name': 'Minkov',
        'picture': 'pet.jpg',
        'address': 'ul. Botev',
        'city': 'Sofia',
        'zip': 1612,
    }
    VALID_BOOK_DATA = {
            'title': 'The Godfather',
            'author': 'Steven King',
            'genre': Book.HISTORY,
            'description': 'Great book!',
            'cover_photo': 'book.jpg',
        }

    def __create_valid_user_and_profile(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )
        return (user, profile)

    def test_create_book__when_all_valid__expect_to_create(self):
        user, profile = self.__create_valid_user_and_profile()

        book = Book.objects.create(
            **self.VALID_BOOK_DATA,
        )
        book.favourites.add(user)
        self.assertIsNotNone(book)
        self.assertEqual(self.VALID_BOOK_DATA['title'], book.title)
        self.assertEqual(self.VALID_BOOK_DATA['author'], book.author)
        self.assertEqual(self.VALID_BOOK_DATA['genre'], book.genre)

    def test_create_profile__when_all_valid__expect_to_redirect_to_details(self):
        user, profile = self.__create_valid_user_and_profile()
        user.save()
        response = self.client.post(
            reverse('create book'),
            data=self.VALID_BOOK_DATA,
        )

        book = Book.objects.get()

        expected_url = reverse('book details', kwargs={'pk': book.pk})
        self.assertRedirects(response, expected_url)
