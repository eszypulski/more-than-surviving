# Generated by Django 4.1.7 on 2023-04-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Activist",
            fields=[
                (
                    "activist_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("event_ids", models.JSONField()),
                ("image_ids", models.JSONField()),
                ("tribal_affiliations", models.JSONField()),
                ("date_of_birth", models.DateField()),
                (
                    "date_of_birth_accuracy",
                    models.CharField(
                        choices=[("DAY", "Day"), ("MONTH", "Month"), ("YEAR", "Year")],
                        default="YEAR",
                        max_length=5,
                    ),
                ),
                (
                    "longitude_of_birth",
                    models.DecimalField(decimal_places=6, max_digits=9),
                ),
                (
                    "latitude_of_birth",
                    models.DecimalField(decimal_places=6, max_digits=9),
                ),
                ("date_of_death", models.DateField()),
                (
                    "date_of_death_accuracy",
                    models.CharField(
                        choices=[("DAY", "Day"), ("MONTH", "Month"), ("YEAR", "Year")],
                        default="YEAR",
                        max_length=5,
                    ),
                ),
                ("short_bio", models.CharField(max_length=100)),
                ("long_bio", models.CharField(max_length=300)),
                ("citations", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "eventid",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=100)),
                ("map", models.BooleanField()),
                ("start_date", models.DateField()),
                (
                    "start_date_accuracy",
                    models.CharField(
                        choices=[("DAY", "Day"), ("MONTH", "Month"), ("YEAR", "Year")],
                        default="YEAR",
                        max_length=5,
                    ),
                ),
                ("end_date", models.DateField()),
                (
                    "end_date_accuracy",
                    models.CharField(
                        choices=[("DAY", "Day"), ("MONTH", "Month"), ("YEAR", "Year")],
                        default="YEAR",
                        max_length=5,
                    ),
                ),
                ("issue_types", models.URLField()),
                ("short_description", models.CharField(max_length=100)),
                ("long_description", models.CharField(max_length=300)),
                ("citations", models.CharField(max_length=300)),
                ("activist_ids", models.JSONField()),
                ("related_event_ids", models.JSONField()),
                ("image_ids", models.JSONField()),
                ("thumbnail_link", models.URLField()),
                ("location_names", models.JSONField()),
                ("location_data", models.JSONField()),
            ],
        ),
    ]
