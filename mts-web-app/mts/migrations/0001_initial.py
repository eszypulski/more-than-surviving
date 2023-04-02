# Generated by Django 4.1.7 on 2023-03-22 21:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "image_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("url", models.URLField()),
                ("alt_text", models.CharField(max_length=100)),
                ("caption", models.CharField(max_length=100)),
                ("credit", models.CharField(max_length=100)),
            ],
        ),
    ]
