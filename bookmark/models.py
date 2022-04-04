from django.db import models

class Bookmark(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField()
