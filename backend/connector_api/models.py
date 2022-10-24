from django.db import models

class User(models.Model):
    """
    User model having fields @name, @gender, @email, @country, @nationality
    """
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    nationality = models.CharField(max_length=15)
