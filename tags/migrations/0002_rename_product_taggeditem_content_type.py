# Generated by Django 5.0.4 on 2024-04-24 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taggeditem',
            old_name='product',
            new_name='content_type',
        ),
    ]
