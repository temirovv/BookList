from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    description = models.TextField(max_length=120)
