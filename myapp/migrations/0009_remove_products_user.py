# Generated by Django 5.0.4 on 2024-07-17 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_products_owner_products_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='user',
        ),
    ]