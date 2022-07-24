from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Recipe(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.PositiveIntegerField(validators=[MinValueValidator(1000000), MaxValueValidator(10000000)])
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Menyu(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
