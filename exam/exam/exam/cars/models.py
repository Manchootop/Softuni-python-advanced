from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from exam.profiles.models import Profile


def check_year(value):
    if value < 1999 or value > 2030:
        raise ValidationError('Year must be between 1999 and 2030!')


def check_image(value):
    if Car.objects.filter(image_url=value).exists():
        raise ValidationError('This image URL is already in use! Provide a new one.')


class CarChoices(models.TextChoices):
    CAR_CHOICE_RALLY = 'Rally'
    CAR_CHOICE_OPEN_WHEEL = 'Open-wheel'
    CAR_CHOICE_KART = 'Kart'
    CAR_CHOICE_DRAG = 'Drag'
    CAR_CHOICE_OTHER = 'Other'


class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=CarChoices.choices,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(1)
        ],
        null=False,
        blank=False,
    )

    year = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1999),
            MaxValueValidator(2030),
            check_year,
        ],
        # help_text='Valid year is a year between 1999 and 2030 (both inclusive).',
    )

    image_url = models.URLField(
        unique=True,
        # help_text='https://...',
        validators=[
            check_image,
        ],
        error_messages={'unique': 'This image URL is already in use! Provide a new one.'}
    )

    price = models.FloatField(
        validators=[MinValueValidator(1.0)],
        null=False,
        blank=False,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def clean(self):
        check_year(self.year)
        check_image(self.image_url)


