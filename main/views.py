from django.shortcuts import render, redirect
import requests
from .models import *
from datetime import datetime

weekday_array = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"]


def home(request):
    return render(request, 'main/home.html')
    
def dashboard(request):
    
    focusesObj = Focus.objects.all()
    exercisesObj = Exercise.objects.all()
    
    a = []
    
    for focus in focusesObj.order_by('name'):
        filtered_exercises = exercisesObj.filter(focus=focus).order_by('name')
        exercise_array = []
        for exercise in filtered_exercises:
            exercise_array += [exercise]
        a += [[focus,exercise_array]]
    
    x = {}
    x['var'] = a
    
    return render(request, 'main/dashboard.html', x)
    
def today(request):
    model_filter_choices = dict(
        monday = Exercise.objects.filter(monday=True),
        tuesday = Exercise.objects.filter(tuesday=True),
        wednesday = Exercise.objects.filter(wednesday=True),
        thursday = Exercise.objects.filter(thursday=True),
        friday = Exercise.objects.filter(friday=True),
        saturday = Exercise.objects.filter(saturday=True),
        sunday = Exercise.objects.filter(sunday=True))
        
    today = datetime.now().date()
    # today_weekday = weekday_array[datetime.now().date().weekday()]
    today_weekday = weekday_array[1]
    today_exercises = model_filter_choices[today_weekday]
    filter_dict = {today_weekday: True}
    
    focusesObj = Focus.objects.all()
    exercisesObj = Exercise.objects.all()
    
    array = []
    
    for focus in focusesObj:
        filtered_exercises = Exercise.objects.filter(focus=focus)
        filtered_exercises = filtered_exercises.filter(**filter_dict)
        exercise_array = []
        for exercise in filtered_exercises:
            doneToday = False
            
            entries_done_today = ExerciseEntry.objects.filter(
                date=today,
                exercise=exercise)
                
            if len(entries_done_today) is not 0:
                doneToday = True
                
            exercise_array += [[exercise,doneToday]]
        if len(exercise_array) is not 0:
            array += [[focus,exercise_array]]
        
    
    x = {}
    x['today_weekday'] = today_weekday.capitalize()
    x['today_exercises'] = today_exercises
    x['var'] = array
    return render(request, 'main/today.html', x)
    
    
    
#==================================================================

def focuses(request):
    x = {}
    x['focuses'] = Focus.objects.all().order_by('name')
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
    x['exercises'] = Exercise.objects.all().order_by('name')
    return render(request, 'main/exercises.html', x)
    
def add_exercise(request):
    if request.method == "POST":
        n = request.POST.get('name')
        f = request.POST.get('focus')
        wi = True if request.POST.get('weight_involved') == "on" else False
        
        sun = True if request.POST.get('sunday') == "on" else False
        mon = True if request.POST.get('monday') == "on" else False
        tue = True if request.POST.get('tuesday') == "on" else False
        wed = True if request.POST.get('wednesday') == "on" else False
        thu = True if request.POST.get('thursday') == "on" else False
        fri = True if request.POST.get('friday') == "on" else False
        sat = True if request.POST.get('saturday') == "on" else False
        
        Exercise.objects.create(
            name = n,
            focus = Focus.objects.get(
                name = f),
            weight_involved = wi,
            sunday = sun,
            monday = mon,
            tuesday = tue,
            wednesday = wed,
            thursday = thu,
            friday = fri,
            saturday = sat)
            
        return redirect('main:exercises')
    else:
        x = {}
        x['focuses'] = Focus.objects.all()
        return render(request, 'main/add_exercise.html', x)

def delete_exercise(request, pk):
    if request.method == "POST":
        Exercise.objects.get(pk=pk).delete()
        return redirect('main:exercises')
    else:
        x = {}
        x['certain_exercise'] = Exercise.objects.get(pk=pk)
        x['certain_pk'] = pk
        return render(request, 'main/delete_exercise.html', x)

#==================================================================
    
def exercise_entries(request):
    x = {}
    x['exercise_entries'] = ExerciseEntry.objects.all()
    return render(request, 'main/exercise_entries.html', x)
    
def add_exercise_entry(request, pk):
    if request.method == "POST":
        d = request.POST.get('date')
        e = Exercise.objects.get(pk=pk)
        w = request.POST.get('weight')
        
        print(d)
        print(e)
        print(w)
        ExerciseEntry.objects.create(
            date = d,
            exercise = e,
            weight = w)
            
        
        return redirect('main:exercise_entries')
    else:
        x = {}
        x['exercise'] = Exercise.objects.get(pk=pk)
        x['today_date'] = str(datetime.now().date())
        print(datetime.now().date())
        return render(request, 'main/add_exercise_entry.html', x)
        
#==================================================================
        


# Create your views here.
