from django.shortcuts import render
import requests
from .models import *

def home(request):
    return render(request, 'main/home.html')
    
def exercises(request):
    x = {}
    x['exercises'] = Exercise.objects.all()
    return render(request, 'main/exercises.html', x)
    
def add_exercise(request):
    if request.method == "POST":
        t = request.POST.get('title')
        print(t)
        f = request.POST.get('focus')
        print(f)
        wi = request.POST.get('weight_involved')
        wi = True if wi == "on" else False
        print(wi)
        
        
        Exercise.objects.create(
            title = t,
            focus = Focus.objects.get(
                name = f),
            weight_involved = wi)
    else:
        x = {}
        x['focuses'] = Focus.objects.all()
        return render(request, 'main/add_exercise.html', x)
    
def exercise_entries(request):
    x = {}
    x['exercise_entries'] = ExerciseEntry.objects.all()
    return render(request, 'main/exerciseEntries.html')

# Create your views here.
