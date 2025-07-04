# todo/forms.py
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'completed']

class EditTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'completed']
