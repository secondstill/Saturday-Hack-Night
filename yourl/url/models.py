
from django.db import models

class UrlData(models.Model):
    url = models.URLField()
    slug = models.CharField(max_length=10, unique=True)
def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"