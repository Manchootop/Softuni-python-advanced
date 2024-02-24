from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def check_username(value):
    is_valid = all(ch.isalnum() or ch == '_' for ch in value)
    if is_valid:
        return None
    raise ValidationError('Username must contain only letters, digits, and underscores!')


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(3, message='Username must be at least 3 chars long!'),
                    check_username],
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(21),
        ],
        help_text='Age requirement: 21 years and above.'
    )

    password = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
