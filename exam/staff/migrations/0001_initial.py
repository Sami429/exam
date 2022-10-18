# Generated by Django 4.1.2 on 2022-10-17 11:33

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("staff_name", models.CharField(max_length=256)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "unique_together": {("phone_number", "email")},
            },
        ),
    ]
