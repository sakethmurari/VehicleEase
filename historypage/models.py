from django.db import models
from django.contrib.auth.models import User
from registerpage.models import Register

# class cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.username



class BookingHistory(models.Model):
    email = models.EmailField(max_length=300)
    type = models.CharField(max_length=100,default='car')
    car_name = models.CharField(max_length=100)
    car_number = models.CharField(max_length=100,default='null',unique=True)
    actual_price = models.IntegerField(default=0)
    price = models.IntegerField()
    days = models.IntegerField()
