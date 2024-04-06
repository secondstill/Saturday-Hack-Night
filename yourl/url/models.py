from django.db import models
class UrlData(models.Model):
    url = models.CharField(max_length=10000)
    slug = models.CharField(max_length=11)
def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"