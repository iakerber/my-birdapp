# Generated by Django 5.1.4 on 2024-12-04 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Waterbird",
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
                ("back_color", models.CharField(max_length=100)),
                ("breast_color", models.CharField(max_length=100)),
                ("bill_size", models.CharField(max_length=100)),
                ("leg_length", models.CharField(max_length=100)),
                ("call_complexity", models.CharField(max_length=100)),
            ],
        ),
    ]
