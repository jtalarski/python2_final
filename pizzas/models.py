from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class RatingChoices(models.IntegerChoices):
    not_rated = 0, 'Not Rated'
    one_star = 1, 'One Star'
    two_star = 2, 'Two Star'
    three_star = 3, 'Three Star'
    four_star = 4, 'Four Star'
    five_star = 5, 'Five Star'
    
class Pizza(models.Model):
    title = models.CharField(max_length=100)
    # TextField datatype allows for more characters than Charfield
    description = models.TextField()
    directions = models.TextField()
    # Relates the recipe to the built-in Django User table based on author. Using cascade with on_delete
    # will remove records from this table if/when the related user is deleted in the User table
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Automatically add date and time that the record was create
    # Provide field for user to select a choice for a rating. ties to class RatingChoice
    current_rating = models.IntegerField(default=RatingChoices.not_rated, choices=RatingChoices.choices)
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
    