from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Pizza(models.Model):
    title = models.CharField(max_length=100)
    # TextField datatype allows for more characters than Charfield
    description = models.TextField()
    directions = models.TextField()
    # Relates the recipe to the built-in Django User table based on author. Using cascade with on_delete
    # will remove records from this table if/when the related user is deleted in the User table
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Automatically add date and time that the record was create
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically add date and time that the record was updated
    updated_at = models.DateTimeField(auto_now=True) 
    
    # String function so that when you output the database object title it is more descriptive
    def __str__(self):   
        return self.title
    
class Rating(models.Model):
    # Create one to many relationship from Pizza to Ratings
    title = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    
    # String function so that when you output the database object title it is more descriptive
    def __str__(self):   
        return self.title
    