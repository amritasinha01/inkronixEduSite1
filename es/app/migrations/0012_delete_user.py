# Generated by Django 4.2.1 on 2023-05-22 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]