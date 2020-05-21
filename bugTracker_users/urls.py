from django.urls import path
from bugTracker_users import views

url_paths = [
    path('/login', views.login_view, name='login')
]
