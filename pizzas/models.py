from typing import Any
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

# Model class that creates allowed rating choices for use in pizza table
class RatingChoice(models.Model):
    user_rating =((0, 'Not Rated'), (1, 'One Star'), (2, 'Two Stars'), (3, 'Three Stars'), (4, 'Four Stars'), (5, "Five Stars"))
    
    # String function so that when you output the database object more descriptive and readable
    def __str__(self):
        return self.user_rating
 
 # Main model class that stores for information about receipes. Is related in a many to one relationship with the User table
 # on author field   
class Pizza(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # TextField datatype allows for more characters than Charfield
    directions = models.TextField()
    # Relates the recipe to the built-in Django User table based on author. Using cascade with on_delete
    # will remove records from this table if/when the related user is deleted in the User table
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Provide field for user to select a choice for a rating. ties to model class RatingChoice
    current_rating = models.IntegerField(default=0, choices=RatingChoice.user_rating)
    calories = models.IntegerField(default=0)
    # Automatically add date and time that the record was created 
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically add date and time that the record was updated
    updated_at = models.DateTimeField(auto_now=True) 
    
    # Function allows user to be redirected after creating or updating a record in the table
    def get_absolute_url(self):
        return reverse("pizza-detail", kwargs={"pk": self.pk})
    
    # String function so that when you output the database object more descriptive and readable
    def __str__(self):   
        return self.title
 
 # Model created for future use to store multiple user ratings for a single pizza.
 # Future planned functionality could allow unauthenticated user to rate any given pizza
 # ratings would be continuously averaged and then displayed in place of author's static rating  
class Rating(models.Model):
    # Create one to many relationship from Pizza to Ratings
    pizza_to_rate = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    
    # Function that redirects user after updating rating field
    def get_absolute_url(self):
        return reverse("pizza-detail", kwargs={"pk": self.pk})
    
    # String function so that when you output the database object more descriptive and readable
    def __str__(self):   
        return self.pizza_to_rate
    
# Model class used to store files uploaded. Note that upload path requires entry in 
# config/settings.py lines 135 and 136
class Submission(models.Model):
    title = models.TextField()
    submission = models.FileField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)    
    
    # String function so that when you output the database object more descriptive and readable
    def __str__(self):   
        return self.title