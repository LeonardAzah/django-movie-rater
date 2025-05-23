from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name