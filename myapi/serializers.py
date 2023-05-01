from rest_framework import serializers
from pizzas import models

# Django rest framework serializer used to convert Python data query responses to datatypes that can be
# used with JSON and other applications
class PizzaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.Pizza
        fields = ['title', 'description', 'directions', 'current_rating', 'author']
        


