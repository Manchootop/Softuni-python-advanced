from django.core import validators
from django.db import models
from django.utils.text import slugify


# Create your models here.


def is_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            return False
    return True


class UserProfile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    # authentication fields:
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=True,
    )

    password = models.CharField(
        max_length=40,
        blank=False,
        null=True,
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=True,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            is_only_letters,
        ],
        blank=False,
        null=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
            is_only_letters,
        ],
        blank=False,
        null=True,
    )

    profile_pic = models.URLField(
        blank=False,
        null=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        default=DO_NOT_SHOW,
        blank=False,
        null=True,
    )


# •	When the user has been deleted, all their photos, pets, comments, and likes should be deleted too
# TODO


class Pet(models.Model):
    PET_NAME_MAX_LENGTH = 30

    name = models.CharField(max_length=PET_NAME_MAX_LENGTH)

    personal_pet_photo = models.URLField()
    date_of_birth = models.DateField(auto_now_add=False)
    slug = models.SlugField()

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super(Pet, self).save(**kwargs)


class PetPhoto(models.Model):
    PHOTO_MAX_SIZE_IN_MEGABYTES = 5.0
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 10
    LOCATION_MAX_LENGTH = 30

    photo = models.ImageField(
        max_size=PHOTO_MAX_SIZE_IN_MEGABYTES * 1024 * 1024,
        blank=True,
        null=True,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=validators.MinLengthValidator(
            DESCRIPTION_MIN_LENGTH,
        ),
        blank=True,
        unique=True,
    )

    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        blank=False,
        null=False,
    )

    tagged_pets = models.ManyToManyField(Pet)

    date_of_publication = models.DateTimeField(auto_now_add=True, auto_now=True)


class Comment(models.Model):
    COMMENT_TEXT_MAX_LENGTH = 300
    comment_text = models.TextField(
        max_length=COMMENT_TEXT_MAX_LENGTH,
    )

    date_of_publication = models.DateTimeField(
        auto_now=True,
    )


class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    liked_photo = models.ForeignKey(PetPhoto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'liked_photo')






