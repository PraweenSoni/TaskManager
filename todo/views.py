# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from accounts.models import NormalUser
from django.contrib import messages

def todo_dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = NormalUser.objects.get(id=user_id)
    todos = Todo.objects.filter(user=user).order_by('-created_at')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            messages.success(request, 'Task added successfully!')
            return redirect('todo_dashboard')
    else:
        form = TodoForm()

    return render(request, 'todo/dashboard.html', {
        'form': form,
        'todos': todos
    })

def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('todo_dashboard')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/edit.html', {'form': form, 'todo': todo})

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('todo_dashboard')
