from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=150, verbose_name="Username")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    password = models.CharField(max_length=128, verbose_name="Password")
    age = models.PositiveIntegerField(verbose_name="Age")
    profession = models.CharField(max_length=100, verbose_name="Profession")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    location = models.CharField(max_length=255, verbose_name="Location")
    landmark = models.CharField(max_length=255, verbose_name="Landmark")

    def __str__(self):
        return self.username