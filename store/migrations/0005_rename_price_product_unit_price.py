# Generated by Django 5.0.4 on 2024-04-24 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]
