# Generated by Django 5.1.4 on 2024-12-15 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("birdid", "0006_alter_raptor_image_bird"),
    ]

    operations = [
        migrations.AlterField(
            model_name="raptor",
            name="image_bird",
            field=models.ImageField(
                blank=True, default="coopers_hawk.jpg", null=True, upload_to="images/"
            ),
        ),
    ]
