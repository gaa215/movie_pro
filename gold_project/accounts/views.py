from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from accounts.forms import CustomUserCreationForm, UserProfileForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Successfully Registered')
            return redirect('login')  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('gold_app:home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required  # Decorate the view with login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)  # Populate form with user's existing data
        if form.is_valid():
            form.save()  # Save the form data
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('gold_app:home')  # Redirect back to the edit profile page after successful update
    else:
        form = UserProfileForm(instance=request.user)  # Create a form with user's existing data
    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        # Delete the user's profile and log out the user
        request.user.delete()
        logout(request)
        return redirect('gold_app:home')  # Redirect to the home page after successful deletion
    return render(request, 'accounts/delete_profile.html')
def logout_view(request):
    # Your logout logic here
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')  # Replace 'home' with the appropriate URL name