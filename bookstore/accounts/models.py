from django import forms
from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from bookstore.accounts.managers import BookstoreUserManager
from bookstore.common.validators import validate_only_letters


class BookstoreUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = BookstoreUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    picture = models.ImageField()

    email = models.EmailField(
        null=True,
        blank=True,
    )

    address = models.CharField(
        max_length=50
    )

    city = models.CharField(
        max_length=50
    )

    zip = models.CharField(
        max_length=5
    )

    user = models.OneToOneField(
        BookstoreUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
