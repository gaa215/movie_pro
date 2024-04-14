from django.contrib import admin

from gold_app.models import Category, Movie


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # Define customizations for Category admin interface here
    list_display = ['name', 'description']  # Customize the fields displayed in the list view
    search_fields = ['name', 'description']  # Enable searching by these fields

admin.site.register(Category, CategoryAdmin)  # Register the custom admin class for Category


class MovieAdmin(admin.ModelAdmin):
    # Define customizations for Movie admin interface here
    list_display = ['name', 'category', 'release_date', 'added_by']  # Customize the fields displayed in the list view
    search_fields = ['name', 'category__name', 'release_date', 'added_by__username']  # Enable searching by these fields
    list_filter = ['category', 'release_date', 'added_by']  # Add filters for these fields

admin.site.register(Movie, MovieAdmin)  # Register the custom admin class for Movie
