from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

class EditNotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
