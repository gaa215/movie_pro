from django.conf import settings
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    description = models.TextField(blank=True)
    release_date = models.DateField()
    actors = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField()

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

