# Generated by Django 4.1.4 on 2023-01-15 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bannaoapp", "0010_order_update_alter_orders_orderedby"),
    ]

    operations = [
        migrations.DeleteModel(
            name="order_update",
        ),
        migrations.RemoveField(
            model_name="orders",
            name="fileName",
        ),
    ]
