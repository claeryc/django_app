from django.shortcuts import render

tasks = ["task-1", "task-2", "task-3"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })