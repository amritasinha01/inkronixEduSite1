# Generated by Django 4.2.1 on 2023-05-25 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0017_delete_post_lecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('youtube_link', models.URLField(blank=True)),
                ('zoom_link', models.URLField(blank=True)),
                ('pdf_file', models.FileField(blank=True, upload_to='pdf_files/')),
                ('word_file', models.FileField(blank=True, upload_to='word_files/')),
                ('internet_link', models.URLField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('create_lecture', 'Can create a lecture'), ('view_my_lecture', 'Can view a lecture')),
            },
        ),
    ]
