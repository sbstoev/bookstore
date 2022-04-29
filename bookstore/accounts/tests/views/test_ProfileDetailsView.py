from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from bookstore.accounts.models import Profile
from bookstore.main.models import Book

UserModel = get_user_model()


class ProfileDetailsViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
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
        # 'favourites': UserModel.objects.create_user(VALID_USER_DATA),
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )
        return (user, profile)

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    # def test_when_opening_not_existing_profile__expect_404(self):
    #     response = self.client.get(reverse('profile details', kwargs={
    #         'pk': 2,
    #     }))
    #
    #     self.assertEqual(404, response.status_code)

    def test_expect_correct_template(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertTemplateUsed('accounts/profile_details.html')

    def test_when_favourites_added__expect_favourites(self):
        # create user and profile:
        user, profile = self.__create_valid_user_and_profile()
        # create book:
        book = Book.objects.create(
            **self.VALID_BOOK_DATA,
        )
        book.favourites.add(user)
        book.save()
        # book = Book.objects.get()
        # self.assertIsNotNone(book)
        favourites = len(Book.objects.filter(favourites=user))
        # response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertEqual(1, favourites)
        # print(response.context_object_name)

    def test_when_no_favourites_added__expect_no_favourites(self):
        # create user and profile:
        user, profile = self.__create_valid_user_and_profile()
        favourites = len(Book.objects.filter(favourites=user))
        self.assertEqual(0, favourites)
        # response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        # self.assertListEqual([], response.context['favourites'])
