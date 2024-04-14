from django.urls import path
from . import views
app_name='admin_panel'

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-or-delete-movie/', views.add_or_delete_movie, name='add_or_delete_movie'),
    path('view-users/', views.view_users, name='view_users'),
    path('delete-users/', views.delete_users, name='delete_users'),
    path('login/', views.admin_login, name='admin_login'),  # New login URL
    path('logout/', views.admin_logout, name='admin_logout'),  # New logout URL
    # Add other URLs for the admin panel as needed
]
