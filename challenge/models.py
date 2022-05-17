from django.db import models
from uuid import uuid4


# Create your models here.
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)

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
