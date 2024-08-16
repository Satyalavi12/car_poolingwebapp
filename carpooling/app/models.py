from django.db import models

class Userdetails(models.Model):
    Name=models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    via = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    car_name = models.CharField(max_length=100)
    start_date_time = models.DateTimeField()
    distance_per_km = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Add this line for the price field

    def __str__(self):
        return f"{self.start} to {self.destination} at {self.start_date_time}"



#location trail
class URL(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url

# models.py
from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')


class Trip(models.Model):
    name = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    via = models.CharField(max_length=100, blank=True)
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    start_time = models.TimeField()

    def __str__(self):
        return self.name
