from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from bookstore.accounts.models import Profile

UserModel = get_user_model()


class ProfileCreateViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qwe',
    }
    VALID_PROFILE_DATA = {
            'first_name': 'Doncho',
            'last_name': 'Minkov',
            'picture': 'man.jpg',
            'address': 'ul. Botev',
            'city': 'Sofia',
            'zip': 1612,
            # 'user': UserModel.objects.create_user(VALID_USER_CREDENTIALS),
        }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def test_create_profile__when_all_valid__expect_to_create(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        self.VALID_PROFILE_DATA['user'] = user
        self.client.post(
            reverse('register'),
            data=self.VALID_PROFILE_DATA,
        )

        profile = Profile.objects.get()
        self.assertIsNotNone(profile)
        # self.assertEqual(self.VALID_PROFILE_DATA['first_name'], profile.first_name)
        # self.assertEqual(self.VALID_PROFILE_DATA['last_name'], profile.last_name)
        # self.assertEqual(self.VALID_PROFILE_DATA['age'], profile.age)

    def test_create_profile__when_all_valid__expect_to_redirect_to_details(self):
        response = self.client.post(
            reverse('create profile'),
            data=self.VALID_PROFILE_DATA,
        )

        profile = Profile.objects.get()

        expected_url = reverse('details profile', kwargs={'pk': profile.pk})
        self.assertRedirects(response, expected_url)