# Generated by Django 5.1.4 on 2024-12-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("birdid", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="waterbird",
            name="water_type",
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
