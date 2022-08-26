# Generated by Django 4.1 on 2022-08-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("number", models.IntegerField(blank=True, null=True)),
                (
                    "profile_pic",
                    models.ImageField(blank=True, upload_to="profile_pics"),
                ),
            ],
        ),
    ]
