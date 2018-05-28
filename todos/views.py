from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Todo


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)


def edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.content = request.POST['content']
        todo.save(update_fields=['title', 'content'])

        return redirect('/todos')
    else:
        return render(request, 'todos/edit.html', {'todo': todo})


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        create_date = timezone.now()

        todo = Todo(title=title, content=content, create_date=create_date)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'todos/add.html')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('/todos')