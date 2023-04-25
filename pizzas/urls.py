from django.urls import path
from . import views

urlpatterns = [
    # For initial function view
    # path('', views.home, name='pizzas-home'),
    # For class view
    path('', views.PizzaListView.as_view(), name='pizzas-home'),
    # Use dynamic URL syntax to pass pizza id
    path('pizza/<int:pk>', views.PizzaDetailView.as_view(), name="pizza-detail"),
    path('recipe/create/', views.PizzaCreateView.as_view(), name='pizzas-create'),
    path('pizza/<int:pk>/update/', views.PizzaUpdateView.as_view(), name="pizzas-update"),
    path('pizza/<int:pk>/delete/', views.PizzaDeleteView.as_view(), name="pizzas-delete"),
    path('about/', views.about, name='about the app'),
]