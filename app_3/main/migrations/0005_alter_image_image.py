# Generated by Django 4.1.5 on 2023-01-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_image_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(upload_to="imgs/"),
        ),
    ]
