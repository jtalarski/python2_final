from . import models
from rest_framework import serializers

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Pizza
        fields = {'title', 'description', 'directions', 'author', 'current_rating'}