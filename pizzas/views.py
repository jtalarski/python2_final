from django.shortcuts import render, HttpResponse

# Builtin Django class views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Builtin Django authorization modules
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# Local module imports
from . import models

# Create your views here.

def home(request):
    pizzas = models.Pizza.objects.all()
    context ={
        "pizzas": pizzas
    }
    return render(request, "pizzas/home.html", context)

def rating(request):
    ratings = models.Rating.objects.all()
    context ={
        "ratings":ratings
    }
    return render(request, "pizzas/ratings_create.html", context)

# Views built off Django default class view
class PizzaListView(ListView):
    model = models.Pizza
    # Override default Django default template name
    template_name = 'pizzas/home.html'
    # Override default Django  database object name
    context_object_name = 'pizzas'
    
class PizzaDetailView(DetailView):
    model = models.Pizza
    
# Only authenticated users will be authorized to create a recipe
class PizzaCreateView(LoginRequiredMixin, CreateView):
    model = models.Pizza
    # Designate fields that you want to expose to user
    fields = ['title', 'description', 'directions']
    
    # Provide the recipe record author since author field is not displayed on form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Only authenticated users will be authorized to update a pizza     
class PizzaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Pizza
    # Designate fields that you want to expose to user
    fields = ['title', 'description']
    
    # Only allow a user to update his own recipe
    def test_fun(self):
        pizza = self.get_object()
        return self.request.user == pizza.author
    
    # Provide the recipe record author since author field is not displayed on form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PizzaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Pizza
    # Redirect the user to the home page after deleting a pizza
    success_url = reverse_lazy('pizzas-home')
    
    # Only allow a user to delete her own recipe
    def test_func(self):
        pizza = self.get_object()
        return self.request.user == pizza.author    
 
# class RatingListView(ListView):
#     model = models.Rating
#     # Override default Django default template name
#     template_name = 'pizzas/home.html'
#     # Override default Django  database object name
#     context_object_name = 'ratings'
    
    
# class RatingCreateView(CreateView):
#     model = models.Rating
#     # Designate fields that you want to expose to user
#     fields = ['title', 'rating']
    
#     # Provide the recipe record author since author field is not displayed on form
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

    
def about(request):
    return render(request, "recipes/about.html", {"title": 'about us'})