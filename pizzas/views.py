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
    fields = ['title', 'description', 'directions', 'current_rating']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PizzaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Pizza.objects.all()
    # Redirect the user to the home page after deleting a pizza
    success_url = reverse_lazy('pizzas-home')
    
    # Only allow a user to delete her own recipe
    def test_func(self):
        pizza = self.get_object()
        return self.request.user == pizza.author    
 

# Generate cookbook text file
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
 
 
# class SubmissionListView(ListView):
#     to_view = models.Submission.objects.all()
#     # Override default Django default template name
#     template_name = 'pizzas/sub_view.html'
#     # Override default Django  database object name
#     context_object_name = 'to_view'
    
class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = models.Submission
    # Designate fields that you want to expose to user
    # template_name = 'submission_form.html'
    fields = ['title', 'submission']
    success_url = reverse_lazy("pizzas-home")
    
              
def about(request):
    return render(request, "pizzas/about.html", {"title": 'about the app'})