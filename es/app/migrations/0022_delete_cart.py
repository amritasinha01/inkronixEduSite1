# Generated by Django 4.2.1 on 2023-05-27 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_rename_course_cart_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
