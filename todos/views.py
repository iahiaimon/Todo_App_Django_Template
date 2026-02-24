from django.shortcuts import render , redirect
from django.http import HttpResponse

from .models import CustomUser , Todo
from .forms import TodoForm , CustomUserForm


# Create your views here.

def todoview(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo.html")  # change to your URL name
    else:
        form = TodoForm()

    todos = Todo.objects.all()
    return render(request, "todo.html", {"form": form, "todos": todos})
