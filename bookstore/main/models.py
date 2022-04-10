from django.db import models


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

    def __str__(self):
        return f'{self.title}'
