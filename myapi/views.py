from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions
from .serializers import PizzaSerializer
from pizzas import models


class PizzaViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Pizza.objects.all()#.order_by('current_rating')
    serializer_class = PizzaSerializer
    filter_backends =(filters.SearchFilter)
    search_fields = ('author', 'title', 'current_rating')

  # Django rest framework class view that serves up queryset returned from database query
  # Query returns all records in table order descending on current rating
class PizzaList(viewsets.ModelViewSet):
    queryset = models.Pizza.objects.all().order_by('-current_rating')
    serializer_class = PizzaSerializer
    permission_classes = [permissions.IsAuthenticated]
            
   
    
    