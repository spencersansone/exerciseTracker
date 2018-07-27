from django.shortcuts import render, redirect
import requests
from .models import *

def home(request):
    return render(request, 'main/home.html')

#==================================================================

def focuses(request):
    x = {}
    x['focuses'] = Focus.objects.all()
    return render(request, 'main/focuses.html', x)

def add_focus(request):
    if request.method == "POST":
        n = request.POST.get('name')
        
        Focus.objects.create(
            name = n)
            
        return redirect('main:focuses')
    else:
        return render(request, 'main/add_focus.html')

def delete_focus(request, pk):
    if request.method == "POST":
        Focus.objects.get(pk=pk).delete()
        return redirect('main:focuses')
    else:
        x = {}
        x['certain_focus'] = Focus.objects.get(pk=pk)
        x['certain_pk'] = pk
        return render(request, 'main/delete_focus.html', x)

#==================================================================

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
        wi = True if request.POST.get('weight_involved') == "on" else False
        print(wi)
        
        
        Exercise.objects.create(
            title = t,
            focus = Focus.objects.get(
                name = f),
            weight_involved = wi)
            
        return redirect('main:exercises')
    else:
        x = {}
        x['focuses'] = Focus.objects.all()
        return render(request, 'main/add_exercise.html', x)

#==================================================================
    
def exercise_entries(request):
    x = {}
    x['exercise_entries'] = ExerciseEntry.objects.all()
    return render(request, 'main/exercise_entries.html', x)
    
def add_exercise_entry(request):
    if request.method == "POST":
        d = request.POST.get('date')
        e = request.POST.get('exercise')
        pass
        return redirect('main:exercise_entries')
    else:
        x = {}
        x['exercises'] = Exercise.objects.all()
        return render(request, 'main/add_exercise_entry.html', x)
        
#==================================================================
        


# Create your views here.
