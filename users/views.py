from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            # Save form data to the User table
            form.save()
            username = form.cleaned_data.get('username')
            # Display visual clue that account creation is successful
            messages.success(request, f"{username}, Account created, please login")
            # Upon success redirect user to site home page
            return redirect("user-login")
    else:
        # Post method is not "POST" redisplay form
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')