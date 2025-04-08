from django.db import models

class vehicle(models.Model):
    name = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=200, default="Car")  # Set a default value
    car_number = models.CharField(max_length=100,default='null',unique=True)
    price = models.IntegerField()
    book = models.BooleanField(default=False)
    picture = models.ImageField(null=True, upload_to='vehicle_items/')

    def __str__(self):
        return self.name

