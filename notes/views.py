from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import NotesForm
from accounts.models import NormalUser
from django.contrib import messages

def notes_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = NormalUser.objects.get(id=user_id)
    note = Notes.objects.filter(user=user).order_by('-created_at')

    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = user
            note.save()
            messages.success(request, 'Note added successfully!')
            return redirect('notes_dashboard')
    else:
        form = NotesForm()

    return render(request, 'notes/dashboard.html', {
        'form': form,
        'note': note
    })

def edit_notes(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Notes updated successfully!', extra_tags='edit-success')
            return redirect('notes_dashboard')
    else:
        form = NotesForm(instance=note)
    return render(request, 'notes/edit.html', {'form': form, 'note': note})

def delete_notes(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.delete()
    messages.success(request, 'Note deleted successfully!')
    return redirect('notes_dashboard')
