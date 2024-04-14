from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Category, Movie
from .forms import CategoryForm
from gold_app.forms import MovieForm

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_panel')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'admin_login.html')
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required
def admin_panel(request):
    return render(request, 'admin_panel.html')

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

@login_required
def add_or_delete_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = MovieForm()
    return render(request, 'add_or_delete_movie.html', {'form': form})

@login_required
def view_users(request):
    users = User.objects.all()
    return render(request, 'view_users.html', {'users': users})

@login_required
def delete_users(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        user.delete()
        return redirect('view_users')
    else:
        return render(request, 'delete_users.html')
