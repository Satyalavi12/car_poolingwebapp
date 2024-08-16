# Generated by Django 5.0.3 on 2024-05-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_rename_distance_userdetails_distance_per_km_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdetails",
            name="price",
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
    ]