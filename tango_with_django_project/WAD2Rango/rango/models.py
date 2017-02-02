from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    maxChar = 128
    name = models.CharField(max_length=maxChar, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=Category.maxChar)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title