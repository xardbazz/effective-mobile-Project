# /home/workdir/project/users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # User interaction
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('delete-account/', views.delete_account, name='delete_account'),
    
    # Mock business resources
    path('projects/', views.mock_projects, name='projects'),
    
    # Admin API for managing permissions (RBAC)
    path('api/roles/', views.RoleListView.as_view(), name='role-list'),
    path('api/permissions/', views.PermissionListView.as_view(), name='permission-list'),
]