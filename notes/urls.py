# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_dashboard, name='notes_dashboard'),
    path('edit/<int:pk>/', views.edit_notes, name='edit_notes'),
    path('delete/<int:pk>/', views.delete_notes, name='delete_notes'),
]
