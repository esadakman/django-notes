# Generated by Django 4.1.1 on 2022-09-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="makale",
            name="yazar",
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]