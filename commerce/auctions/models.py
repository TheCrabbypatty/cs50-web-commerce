from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class User(AbstractUser):
    pass

class Catagory(models.TextChoices):
    FASH = "FASH", "Fashion"
    HOME = "HOME", "Home and Garden"
    ELEC = "ELEC", "Electronics"
    TOYS = "TOYS", "Toys and Games"
    SPRT = "SPRT", "Sports and Outdoors"
    BEAU = "BEAU", "Beauty and Personal Care"
    ARTS = "ARTS", "Arts and Crafts"
    PETS = "PETS", "Pet Supplies"
    OFFC = "OFFC", "Office Supplies"

class Listing(models.Model):
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "listings_created")
    title = models.CharField(max_length = 64, blank = False)
    description = models.CharField(max_length=1000)
    current_price = models.IntegerField(null=True, blank=True) 
    starting_bid = models.IntegerField(blank = False)
    catagory = models.CharField(max_length = 23, choices = Catagory.choices)
    image_url = models.URLField(blank = True)
    active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="listings_won")
    watchlist = models.BooleanField(default = False)
        
    def __str__(self):
        return f"{self.title}"


class Bid(models.Model):
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE)
    value = models.DecimalField(blank = False, max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(default = timezone.now)

    def clean(self):
        if self.value < self.listing.current_price:
            raise ValidationError("Bid cannot be below starting bid.")
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bid of ${self.value} by {self.creator} on {self.listing}"


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE)
    contents = models.CharField(max_length = 1000)
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.creator} comment on {self.listing}"

