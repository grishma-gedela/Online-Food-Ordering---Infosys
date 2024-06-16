from django.db import models
from customer.models import CustomUser  # Import CustomUser from the user app
from phonenumber_field.modelfields import PhoneNumberField

class restaurantUser(CustomUser):
    restaurantName = models.CharField(max_length=50)
    address = models.TextField()
    restaurantContact = PhoneNumberField()


class foodItems(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    restaurantName = models.CharField(max_length=50)