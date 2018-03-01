from django.db import models
from cuser.models import AbstractCUser
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser

class Review(models.Model):
    rating = models.IntegerField
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

class User(AbstractCUser):
    school = models.TextField(blank = True, null = True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
