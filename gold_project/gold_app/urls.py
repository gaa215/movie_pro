from django.urls import path
from . import views

app_name = 'gold_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_id>/', views.movie, name='movie'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('unauthorized/', views.unauthorized_access, name='unauthorized_access'),
    path('category/<int:category_id>/', views.category_movies, name='category_movies'),
    path('categories/', views.category_list, name='category_list'),  # Add this line
]
