# Generated by Django 5.0.3 on 2024-05-03 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_mymodel"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userdetails",
            old_name="distance",
            new_name="distance_per_km",
        ),
        migrations.RemoveField(
            model_name="userdetails",
            name="price",
        ),
    ]
