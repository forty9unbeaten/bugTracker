from django.urls import path
from bugTracker_users import views

url_paths = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/new', views.new_user_view, name='new_user')
]
