# Generated by Django 5.0.4 on 2024-04-15 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_products_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='owner',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='myapp.users'),
        ),
    ]