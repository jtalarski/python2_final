from rest_framework import serializers
from pizzas import models


class PizzaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.Pizza
        fields = ['title', 'description', 'directions', 'current_rating', 'author']
        


