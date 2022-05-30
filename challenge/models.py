from django.db import models
from uuid import uuid4


# Create your models here.
from rest_framework import serializers


def upload_writer_image(instance, filename):
    return f'{instance.id}-{filename}'


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=upload_writer_image, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=300)
    summary = models.TextField()
    first_paragraph = models.TextField()
    body = models.TextField()

    def clean(self):
        if len(self.body) < 50:
            raise serializers.ValidationError({'body': 'body need to have at least 50 digits'})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
