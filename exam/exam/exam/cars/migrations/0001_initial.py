# Generated by Django 5.0.2 on 2024-02-24 09:25

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Rally', 'Car Choice Rally'), ('Open-wheel', 'Car Choice Open Wheel'), ('Kart', 'Car Choice Kart'), ('Drag', 'Car Choice Drag'), ('Other', 'Car Choice Other')], max_length=10)),
                ('model', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(1)])),
                ('year', models.PositiveSmallIntegerField(help_text='Valid year is a year between 1999 and 2030 (both inclusive).', validators=[django.core.validators.MinValueValidator(1999), django.core.validators.MaxValueValidator(2030)])),
                ('image_url', models.URLField(error_messages={'unique': 'This image URL is already in use! Provide a new one.'}, help_text='https://...', unique=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]