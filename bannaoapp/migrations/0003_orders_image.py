# Generated by Django 4.1.4 on 2023-01-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bannaoapp", "0002_remove_orders_timedate"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]
