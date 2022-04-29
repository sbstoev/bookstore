from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from bookstore.common.validators import validate_only_letters


class Book(models.Model):
    # Constants
    PSYCHOLOGY = "Psychology"
    PHILOSOPHY = "Philosophy"
    POETRY = "Poetry"
    HISTORY = "History"
    FICTION = "Fiction"
    OTHER = "Other"

    GENRES = [(x, x) for x in (PSYCHOLOGY, PHILOSOPHY, POETRY, HISTORY, FICTION, OTHER)]
    TITLE_MAX_LENGTH = 100
    AUTHOR_MAX_LENGTH = 50

    # Fields(Columns):
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    author = models.CharField(
        max_length=AUTHOR_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=max(len(x) for (x, _) in GENRES),
        choices=GENRES,
    )

    description = models.TextField(
        null=True,  # because it is optional
        blank=True,  # so it works with administration
    )

    cover_photo = models.ImageField(
        # validators=(
        #     validate_file_max_size_in_mb(5),
        # )
    )

    favourites = models.ManyToManyField(
        get_user_model(),
    )

    def __str__(self):
        return f'{self.title}'


class Author(models.Model):
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

    picture = models.URLField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    link = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Event(models.Model):
    TITLE_MAX_LENGTH = 100
    LOCATION_MAX_LENGTH = 50

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    date = models.DateField(
        null=True,
        blank=True,
    )

    city = models.CharField(
        max_length=LOCATION_MAX_LENGTH
    )

    country = models.CharField(
        max_length=LOCATION_MAX_LENGTH
    )

    picture = models.URLField(
        null=True,
        blank=True,
    )

    link = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.title}'
