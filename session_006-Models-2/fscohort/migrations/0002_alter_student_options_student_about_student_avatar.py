# Generated by Django 4.1 on 2022-08-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fscohort", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={"ordering": ["number"], "verbose_name_plural": "Öğrenciler"},
        ),
        migrations.AddField(
            model_name="student",
            name="about",
            field=models.TextField(blank=True, null=True, verbose_name="Hakkinda"),
        ),
        migrations.AddField(
            model_name="student",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/", verbose_name="Resim"
            ),
        ),
    ]