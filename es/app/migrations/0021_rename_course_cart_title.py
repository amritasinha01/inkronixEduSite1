# Generated by Django 4.2.1 on 2023-05-27 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='course',
            new_name='title',
        ),
    ]
