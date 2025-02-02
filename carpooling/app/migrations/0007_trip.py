# Generated by Django 5.0.3 on 2024-05-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_userdetails_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trip",
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
                ("name", models.CharField(max_length=100)),
                ("start", models.CharField(max_length=100)),
                ("via", models.CharField(blank=True, max_length=100)),
                ("destination", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("start_time", models.TimeField()),
            ],
        ),
    ]
