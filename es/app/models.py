from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.urls import reverse

import os



# Create your models here.



class allCategory(models.Model):
    name = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to='book_images', default='default_image.jpg')

    def __str__(self):
        return self.name



class subCourse(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    bookcount = models.BooleanField(default=False)
    category = models.ForeignKey('allCategory', on_delete=models.CASCADE)
    popularity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='book_images/', default='default_book_image.jpg')
    featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    discounted_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)  # Add the discounted price field

    def __str__(self):
        return self.title



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_link = models.URLField(blank=True)
    zoom_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])



class Lecture(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_link = models.URLField(blank=True)
    zoom_link = models.URLField(blank=True)
    pdf_file = models.FileField(upload_to='pdf_files/', blank=True)
    word_file = models.FileField(upload_to='word_files/', blank=True)
    internet_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lecture_detail', args=[str(self.pk)])

    class Meta:
        permissions = (
            ('create_lecture', 'Can create a lecture'),
            ('view_my_lecture', 'Can view a lecture'),
        )




class Lecture2(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_link = models.URLField(blank=True)
    zoom_link = models.URLField(blank=True)
    pdf_file = models.FileField(upload_to='pdf_files/', blank=True)
    word_file = models.FileField(upload_to='word_files/', blank=True)
    internet_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lecture_detail', args=[str(self.pk)])

    class Meta:
        permissions = (
            ('create_lecture', 'Can create a lecture'),
            ('view_my_lecture', 'Can view a lecture'),
        )





class Lecture3(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_link = models.URLField(blank=True)
    zoom_link = models.URLField(blank=True)
    pdf_file = models.FileField(upload_to='pdf_files/', blank=True)
    word_file = models.FileField(upload_to='word_files/', blank=True)
    internet_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lecture_detail', args=[str(self.pk)])

    class Meta:
        permissions = (
            ('create_lecture', 'Can create a lecture'),
            ('view_my_lecture', 'Can view a lecture'),
        )

class Lecture4(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_link = models.URLField(blank=True)
    zoom_link = models.URLField(blank=True)
    pdf_file = models.FileField(upload_to='pdf_files/', blank=True)
    word_file = models.FileField(upload_to='word_files/', blank=True)
    internet_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lecture_detail', args=[str(self.pk)])

    class Meta:
        permissions = (
            ('create_lecture', 'Can create a lecture'),
            ('view_my_lecture', 'Can view a lecture'),
        )






class Cart(models.Model):
    category = models.ForeignKey('allCategory', on_delete=models.CASCADE, unique=True)
    # Add other fields as needed

    def __str__(self):
        return str(self.category)

    def clean(self):
        if not self.category:
            raise models.ValidationError("Category is required.")


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

