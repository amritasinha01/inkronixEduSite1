# Generated by Django 4.2.1 on 2023-05-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_book_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookcount',
            field=models.BooleanField(default=False),
        ),
    ]