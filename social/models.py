from django.db import models
from django.contrib.auth.models import AbstractUser


# Using AbstractUser class to inherit from for user authentication
class User(AbstractUser):
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='social_user_set',  # Change this name
    #     blank=True,
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='social_user_permissions_set',  # Change this name
    #     blank=True,
    # )
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='account_images/', blank=True, null=True)
    job = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=11, null=True, blank=True)