from django.shortcuts import render, HttpResponse, redirect

# Builtin Django class views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Builtin Django authorization modules
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
import pandas as pd
from django.contrib.auth.models import User

# Import Bokeh modules and other plotting modules
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN



# Local module imports
from . import models

# Create your views here.

# Simple function view that allows readonly access to all records from pizza table
def home(request):
    pizzas = models.Pizza.objects.all()
    submissions = models.Submission.object.all()
    context ={
        "pizzas": pizzas,
        "submissions": submissions,
    }
    return render(request, "pizzas/home.html", context)

def rating(request):
    ratings = models.Rating.objects.all()
    context ={
        "ratings":ratings
    }
    return render(request, "pizzas/ratings_create.html", context)

# Views built off Django default class views

# listview Django class view that allows readonly access to all records from pizza table
class PizzaListView(ListView):
    model = models.Pizza
    # Override default Django default template name
    template_name = 'pizzas/home.html'
    # Override default Django  database object name
    context_object_name = 'pizzas'
    
# Detailview Django class view that allows readonly and authenticated views of a single record in the pizza table
class PizzaDetailView(DetailView):
    model = models.Pizza
    
# Createview class view that allows only authenticated user to create a new record in the pizza table. Template will 
# redirect unauthenticated users to login
class PizzaCreateView(LoginRequiredMixin, CreateView):
    model = models.Pizza
    # Designate fields that you want to expose to user
    fields = ['title', 'description', 'directions']
    
    # Provide the recipe record author since author field is not displayed on form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Updateview Django class view that allows only authenticated users to update a record in the pizza table   
class PizzaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Pizza
    fields = ['title', 'description', 'directions', 'current_rating']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Deleteview Django class view that allows only authenticated users to delete a record in the pizza table
class PizzaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Pizza.objects.all()
    # Redirect the user to the home page after deleting a pizza
    success_url = reverse_lazy('pizzas-home')
    
    # Only allow a user to delete her own recipe
    def test_func(self):
        pizza = self.get_object()
        return self.request.user == pizza.author    
 

# Hidden function view allows user to print all records from the pizza table
def recipe_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=recipe.txt'
    
    # Designate model
    to_print = models.Pizza.objects.all().filter()
    # success_url = reverse_lazy('pizzas-home')
    
    # Create blank list
    lines = []
    
    # Loop through query
    for recipe in to_print:
        lines.append(f'__{recipe.title}__\n\n{recipe.description}\n\ndirections:\n{recipe.directions}\n\nrating: {recipe.current_rating}  chef: {recipe.author}\n\n\n')
        
    response.writelines(lines)
    return response
 
 # Create views that would allow a guest user to upload a recipe text file 
 # In future iteration I would use regex to search through file and pull out
 # strings that could be used to populate database  
class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = models.Submission
    # Designate fields that you want to expose to user
    # template_name = 'submission_form.html'
    fields = ['title', 'submission']
    
    
    success_url = reverse_lazy("pizzas-home")
 
class SubmissionListView(LoginRequiredMixin, ListView):
    model = models.Submission
    # Override default Django default template name
    template_name = 'pizzas/sub_home.html'
    # Override default Django  database object name
    context_object_name = 'submissions'
    
class SubmissionDetailView(LoginRequiredMixin, DetailView):
    model = models.Submission
    
# Hidden views to create charts
def graph3(request):
    
    
    plot = figure(title = "Amount of sleep throughout my work week")
    y =[1, 2, 3, 4, 5]
    x =[8, 5, 5, 6, 8]
    plot.line(y,x)

    script, div = components(plot, CDN)    
    return render(request, "pizzas/popular.html", {"the_script": script, "the_div": div})
                          
# Simple function view that displays a readonly html file with a description of the site/application                   
def about(request):
    return render(request, "pizzas/about.html", {"title": 'about the app'})