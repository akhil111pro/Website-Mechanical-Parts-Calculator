# Generated by Django 4.1.4 on 2023-01-01 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bannaoapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orders",
            name="timeDate",
        ),
    ]