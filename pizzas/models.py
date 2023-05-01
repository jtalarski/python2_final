from typing import Any
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class RatingChoice(models.Model):
    user_rating =((0, 'Not Rated'), (1, 'One Star'), (2, 'Two Stars'), (3, 'Three Stars'), (4, 'Four Stars'), (5, "Five Stars"))
    
    def __str__(self):
        return self.user_rating
    
class Pizza(models.Model):
    title = models.CharField(max_length=100)
    # TextField datatype allows for more characters than Charfield
    description = models.CharField(max_length=200)
    directions = models.TextField()
    # Relates the recipe to the built-in Django User table based on author. Using cascade with on_delete
    # will remove records from this table if/when the related user is deleted in the User table
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Automatically add date and time that the record was create
    # Provide field for user to select a choice for a rating. ties to class RatingChoice
    current_rating = models.IntegerField(default=0, choices=RatingChoice.user_rating)
    
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically add date and time that the record was updated
    updated_at = models.DateTimeField(auto_now=True) 
    
    # String function so that when you output the database object title it is more descriptive
    
    def get_absolute_url(self):
        return reverse("pizza-detail", kwargs={"pk": self.pk})
    
    def __str__(self):   
        return self.title, self.author
    
class Rating(models.Model):
    # Create one to many relationship from Pizza to Ratings
    pizza_to_rate = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    
    def get_absolute_url(self):
        return reverse("pizza-detail", kwargs={"pk": self.pk})
    
    # String function so that when you output the database object title it is more descriptive
    def __str__(self):   
        return self.pizza_to_rate
    
class Submission(models.Model):
    title = models.TextField()
    submission = models.FileField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):   
        return self.title