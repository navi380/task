from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from django.contrib.auth.models import User

ITEM_CHOICES = (
    ('lost', 'lost'),
    ('found', 'found'),
)

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    status = models.CharField(choices=ITEM_CHOICES, max_length=30)
    email = models.EmailField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '03000420271'. Up to 13 digits allowed.")
    phone_number = models.BigIntegerField(validators=[phone_regex])

    def __str__(self):
        return self.item_name

class Images(models.Model):
    item_val = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_images")
    image = models.ImageField(upload_to="Item")

    def __str__(self):
        return self.item_val.item_name