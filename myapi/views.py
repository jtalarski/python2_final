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

  
class PizzaList(viewsets.ModelViewSet):
    # queryset = models.Pizza.objects.all()#.order_by('current_rating')
    serializer_class = PizzaSerializer
    
    def get_queryset(self):
        queryset = models.Pizza.objects.all()
        author = self.request.QUERY_PARAMS.get('author', None)
        if author is not None:
            queryset = queryset.filter(pizza__author='author')
        
   
    
    