from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from gold_app.forms import MovieForm
from gold_app.models import Movie, Category

@login_required()
def home(request):
    movie = Movie.objects.all()
    categories = Category.objects.all()
    context = {'movie_list': movie,
               'categories': categories
               }
    return render(request, 'gold_app/home.html', context)

@login_required()
def movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie.html', {'movie': movie})

@login_required()
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user  # Associate the current user with the movie
            movie.save()
            return redirect('gold_app:home')  # Redirect to the home page after adding a movie
    else:
        form = MovieForm()
    return render(request, 'add.html', {'form': form})

@login_required()
def update(request, id):
    movie = get_object_or_404(Movie, id=id)

    # Check if the current user is the owner of the movie
    if request.user != movie.added_by:
        # If not, redirect or display a message indicating unauthorized access
        return redirect('gold_app:unauthorized_access')  # You need to define this URL

    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('gold_app:home')  # Redirect to the home page after updating a movie

    return render(request, 'edit.html', {'form': form, 'movie': movie})

@login_required()
def delete(request, id):
    movie = get_object_or_404(Movie, id=id)

    # Check if the current user is the owner of the movie
    if request.user != movie.added_by:
        # If not, redirect or display a message indicating unauthorized access
        return redirect('gold_app:unauthorized_access')  # You need to define this URL

    if request.method == 'POST':
        movie.delete()
        return redirect('gold_app:home')  # Redirect to the home page after deleting a movie

    return render(request, 'delete.html', {'movie': movie})

def unauthorized_access(request):
    return render(request, 'unauthorized.html')

from django.shortcuts import render
from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


@login_required()
def category_movies(request, category_id):
    # Retrieve the category object based on the category_id provided in the URL
    category = get_object_or_404(Category, id=category_id)

    # Retrieve all movies belonging to the specified category
    movies = Movie.objects.filter(category=category)

    # Render the category_movies.html template with the category and movies
    return render(request, 'category_movies.html', {'category': category, 'movies': movies})