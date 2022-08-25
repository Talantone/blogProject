import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image = models.ImageField()
    publish_date = models.DateTimeField(default=datetime.datetime.now())
    for_logged_users = models.BooleanField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
