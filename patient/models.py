from django.db import models
from django.contrib.auth.models import AbstractUser
class patient(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=16)
    image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)
    def __str__(self):
        return self.name