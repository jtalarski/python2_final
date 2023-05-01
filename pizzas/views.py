# Import builtin Django site navigation shortcut modules 
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy

# Import builtin Django generic class view modules. Provides low code options for serving
# data queryset results
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Builtin Django authorization mixin modules assisting with user authentication and authorization
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Import pandas data manipulation and output module
import pandas as pd

# Import Bokeh modules and other plotting modules
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN

# Local module imports
from django.contrib.auth.models import User
from . import models

# Create your views here.

# Simple function view that houses context objects that can be passed to other urls. Context for submission and
# querysets referenced here for code cleanliness and organization only. Only the pizzas context is render in
# this view. Pizzas context object is used in multiple class views
def home(request):
    pizzas = models.Pizza.objects.all()
    submissions = models.Submission.object.all()
    ratings = models.Rating.objects.all()
    context ={
        "pizzas": pizzas,
        "submissions": submissions,
        "ratings": ratings,
    }
    return render(request, "pizzas/home.html", context)

# Views built off Django default class views

# listview Django class view that allows readonly access to all records from pizza table
class PizzaListView(ListView):
    model = models.Pizza
    # Override default Django default template name
    template_name = 'pizzas/home.html'
    # Override default Django  database object name
    context_object_name = 'pizzas'
    
# Detailview Django class view that allows readonly and authenticated views of a single record in the 
# pizza table
class PizzaDetailView(DetailView):
    model = models.Pizza
    
# Createview class view that allows only authenticated user to create a new record in the pizza table. 
# Template will redirect unauthenticated users to login based on universal login url defined in
# config.setting.py
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
    
    # Optional reverse_lazy redirect url. Not needed since print functionality
    # open users default text editor
    # success_url = reverse_lazy('pizzas-home')
    
    # Create blank list
    lines = []
    
    # Loop through query
    for recipe in to_print:
        lines.append(f'__{recipe.title}__\n\n{recipe.description}\n\ndirections:\n{recipe.directions}\n\nrating: {recipe.current_rating}  chef: {recipe.author}\n\n\n')
     
    # Write each line to tet file   
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
    
    # Default reverse_lazy redirect url that sends user to home page after upload
    success_url = reverse_lazy("pizzas-home")
 
# FUTURE USE - Builtin Django class view that lists all files uploaded to site.
# A similar view can be accessed from the Django admin console
class SubmissionListView(LoginRequiredMixin, ListView):
    model = models.Submission
    # Override default Django default template name
    template_name = 'pizzas/sub_home.html'
    # Override default Django  database object name
    context_object_name = 'submissions'
 
# FUTURE USE - Builtin Django detail view that provides access to a single uploaded
# file. A similar view can be accessed from the Django admin console   
class SubmissionDetailView(LoginRequiredMixin, DetailView):
    model = models.Submission
    
# Hidden views to create charts
def graph3(request):
    
    # Create pandas dataframe from model query
    pizza_rate = models.Pizza.objects.all().values('title', 'current_rating')
    df_pizza = pd.DataFrame(list(pizza_rate))
    # print(df_pizza.to_string()) - TESTING ONLY
    
    # Set variable and figure display parameters for plotting
    pizzas = df_pizza['title'].values.tolist()
    top = df_pizza['current_rating'].values.tolist()
    plot = figure(title = "Current Pizza Ratings Chart", x_range=pizzas)
    plot.vbar(x=pizzas, top = top, width=0.5)
    
    # defines object to pass to Bokeh code on listed html templates    
    script, div = components(plot, CDN)    
    return render(request, "pizzas/graph3.html", {"the_script": script, "the_div": div})

def graph4(request):
     
    # Create pandas dataframe from model query 
    calories_slice = models.Pizza.objects.all().values('title','calories')
    df_calories = pd.DataFrame(list(calories_slice))
    
    # Set variable and figure display parameters for plotting
    pizzas = df_calories['title'].values.tolist()
    top = df_calories['calories'].values.tolist()
    plot = figure(title = "Current Pizza Ratings Chart", x_range=pizzas)
    plot.vbar(x=pizzas, top = top, width=0.5)
    
    # defines object to pass to Bokeh code on listed html templates  
    script, div = components(plot, CDN)    
    return render(request, "pizzas/graph3.html", {"the_script": script, "the_div": div})
                              
# Simple function view that displays a readonly html file with a description of the site/application                   
def about(request):
    return render(request, "pizzas/about.html", {"title": 'about the app'})


    
    