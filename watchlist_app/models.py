from tkinter.constants import CASCADE

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=120)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    active=models.BooleanField(default=True)
    platform =models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rating