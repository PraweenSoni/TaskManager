# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_dashboard, name='todo_dashboard'),
    path('edit/<int:pk>/', views.edit_todo, name='edit_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
]
