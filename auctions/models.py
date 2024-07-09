from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length = 80)
    description = models.TextField(max_length = 500)
    datentime =  models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()
    image = models.TextField(max_length=400, blank=True)
    category = models.TextField(max_length=50, blank=True)
    starting_bid = models.IntegerField()

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="items")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


class Bids(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    bid = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()

class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(max_length = 600)






