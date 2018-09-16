from django.shortcuts import render, redirect
import requests
from .models import *
from datetime import datetime, timedelta
from django.db.models import Q

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
    
def help(request):
    return render(request, 'main/help.html')
    
def dashboard(request):
    
    focusesObj = ExerciseFocus.objects.all()
    exercisesObj = Exercise.objects.all()
    
    a = []
    
    for focus in focusesObj.order_by('name'):
        filtered_exercises = exercisesObj.filter(exercise_focus=focus).order_by('name')
        exercise_array = []
        for exercise in filtered_exercises:
            exercise_array += [exercise]
        a += [[focus,exercise_array]]
    
    x = {}
    x['var'] = a
    
    return render(request, 'main/dashboard.html', x)
    
def routine(request):
    
    exercisesObj = Exercise.objects.all()
    
    su,m,tu,w,th,f,sa = [],[],[],[],[],[],[]
    
    for exercise in exercisesObj:
        if exercise.sunday is True:
            su += [exercise]
        if exercise.monday is True:
            m += [exercise]
        if exercise.tuesday is True:
            tu += [exercise]
        if exercise.wednesday is True:
            w += [exercise]
        if exercise.thursday is True:
            th += [exercise]
        if exercise.friday is True:
            f += [exercise]
        if exercise.saturday is True:
            sa += [exercise]
            
            
    
    array = [
        [weekday_array[6].capitalize(),su],
        [weekday_array[0].capitalize(),m],
        [weekday_array[1].capitalize(),tu],
        [weekday_array[2].capitalize(),w],
        [weekday_array[3].capitalize(),th],
        [weekday_array[4].capitalize(),f],
        [weekday_array[5].capitalize(),sa]]
        
        
    x = {}
    x['array'] = array
    return render(request, 'main/routine.html', x)
    
def today(request):
    today = datetime.now().date()
    if request.method == 'POST':
        pass
        certain_exercise_id = request.POST.get('exercise_id') 
        certain_exercise = Exercise.objects.get(id=certain_exercise_id)
        
        attribute_d = {
            'date': today,
            'exercise': certain_exercise
        }
        
        if certain_exercise.weight:
            w = float(request.POST.get('weight'))
            attribute_d['weight'] =  w
        if certain_exercise.miles:
            m = float(request.POST.get('miles'))
            attribute_d['miles'] =  m
        if certain_exercise.time:
            hours = int(request.POST.get('hours'))
            minutes = int(request.POST.get('minutes'))
            seconds = int(request.POST.get('seconds'))
            t = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            
            attribute_d['time'] =  t
        if certain_exercise.laps:
            l = int(request.POST.get('laps'))
            attribute_d['laps'] = l
        if certain_exercise.reps:
            r = int(request.POST.get('reps'))
            attribute_d['reps'] =  r
        if certain_exercise.sets:
            s = int(request.POST.get('sets'))
            attribute_d['sets'] =  s
            
        ExerciseEntry.objects.create(**attribute_d)
        
        return redirect('main:today')
    else:
        today_weekday = weekday_array[today.weekday()]
        all_focuses = ExerciseFocus.objects.all()
        all_exercises = Exercise.objects.all()
        l = []
        
        for focus in all_focuses:
            filtered_exercises = all_exercises.filter(
                Q(**{today_weekday: True}) & Q(exercise_focus=focus))
            exercise_l = []
            
            for exercise in filtered_exercises:
                entries_done_today = ExerciseEntry.objects.filter(
                    date=today,
                    exercise = exercise,)
                
                if len(entries_done_today) != 0:
                    doneToday = True
                else:
                    doneToday = False
                    
                exercise_l += [[exercise,doneToday]]
                
            if len(exercise_l) != 0:
                l += [[focus,exercise_l]]
        x = {}
        x['today_weekday'] = today_weekday.capitalize()
        x['var'] = l
        return render(request, 'main/today.html', x)
    
# def OLD_today(request):
#     today = datetime.now().date()
#     today_weekday = weekday_array[today.weekday()]
#     filter_dict = {today_weekday: True}
    
#     focusesObj = ExerciseFocus.objects.all()
#     exercisesObj = Exercise.objects.all()
    
#     array = []
    
#     for focus in focusesObj:
#         filtered_exercises = Exercise.objects.filter(exercise_focus=focus)
#         filtered_exercises = filtered_exercises.filter(**filter_dict)
#         exercise_array = []
#         for exercise in filtered_exercises:
#             doneToday = False
            
#             entries_done_today = ExerciseEntry.objects.filter(
#                 date=today,
#                 exercise=exercise)
#             print(entries_done_today)
                
#             if len(entries_done_today) is not 0:
#                 doneToday = True
                
#             exercise_array += [[exercise,doneToday]]
#         if len(exercise_array) is not 0:
#             array += [[focus,exercise_array]]
#     x = {}
#     x['today_weekday'] = today_weekday.capitalize()
#     x['var'] = array
#     return render(request, 'main/today.html', x)
            
#     if request.method == "POST":
#         e_id = request.POST.get('exercise_id') 
#         exerciseObj = Exercise.objects.get(id=e_id)
        
#         if exerciseObj.weight_involved:
#             w = request.POST.get('weight')
            
#             ExerciseEntry.objects.create(
#                 date = today,
#                 exercise = exerciseObj,
#                 weight = w)
#                 # this works!
#         elif exerciseObj.cardio_type:
#             if exerciseObj.cardio_type.name == "Miles and Time":
#                 m = request.POST.get('miles')
#                 t = request.POST.get('time')
                
#                 ExerciseEntry.objects.create(
#                     date = today,
#                     exercise = exerciseObj,
#                     miles = m,
#                     time = timedelta(hours=int(t)))
#                     # so far so good, still need to change timedelta
                    
#             elif exerciseObj.cardio_type.name == "Reps and Sets":
#                 r = request.POST.get('reps')
#                 s = request.POST.get('sets')
                
#                 ExerciseEntry.objects.create(
#                     date = today,
#                     exercise = exerciseObj,
#                     reps = r,
#                     sets = s)
                    
#             elif exerciseObj.cardio_type.name == "Swimming":
#                 t = request.POST.get('time')
#                 l = request.POST.get('laps')
                
#                 ExerciseEntry.objects.create(
#                     date = today,
#                     exercise = exerciseObj,
#                     time = timedelta(hours=int(t)),
#                     laps = l)
#         else:
#             ExerciseEntry.objects.create(
#                 date = today,
#                 exercise = exerciseObj)
            
#         return redirect('main:today')
#     else:
#         today = datetime.now().date()
#         today_weekday = weekday_array[today.weekday()]
#         filter_dict = {today_weekday: True}
        
#         focusesObj = ExerciseFocus.objects.all()
#         exercisesObj = Exercise.objects.all()
        
#         array = []
        
#         for focus in focusesObj:
#             filtered_exercises = Exercise.objects.filter(exercise_focus=focus)
#             filtered_exercises = filtered_exercises.filter(**filter_dict)
#             exercise_array = []
#             for exercise in filtered_exercises:
#                 doneToday = False
                
#                 entries_done_today = ExerciseEntry.objects.filter(
#                     date=today,
#                     exercise=exercise)
#                 print(entries_done_today)
                    
#                 if len(entries_done_today) is not 0:
#                     doneToday = True
                    
#                 exercise_array += [[exercise,doneToday]]
#             if len(exercise_array) is not 0:
#                 array += [[focus,exercise_array]]
#         x = {}
#         x['today_weekday'] = today_weekday.capitalize()
#         x['var'] = array
#         return render(request, 'main/today.html', x)
        
def tomorrow(request):
    tomorrow = datetime.now().date() + timedelta(days=1)
    tomorrow_weekday = weekday_array[tomorrow.weekday()]
    
    filter_dict = {tomorrow_weekday: True}
    
    tomorrow_exercises = Exercise.objects.filter(**filter_dict)
    
    x = {}
    x['tomorrow_weekday'] = tomorrow_weekday.capitalize()
    x['tomorrow_exercises'] = tomorrow_exercises
    return render(request, 'main/tomorrow.html', x)
    
    
    
    
#==================================================================

def exercise_focuses(request):
    x = {}
    x['exercise_focuses'] = ExerciseFocus.objects.all().order_by('name')
    return render(request, 'main/exercise_focuses.html', x)

def add_exercise_focus(request):
    if request.method == "POST":
        n = request.POST.get('name')
        
        ExerciseFocus.objects.create(
            name = n)
            
        return redirect('main:exercise_focuses')
    else:
        return render(request, 'main/add_exercise_focus.html')

def delete_exercise_focus(request, pk):
    if request.method == "POST":
        ExerciseFocus.objects.get(pk=pk).delete()
        return redirect('main:exercise_focuses')
    else:
        x = {}
        x['certain_exercise_focus'] = ExerciseFocus.objects.get(pk=pk)
        x['certain_pk'] = pk
        return render(request, 'main/delete_exercise_focus.html', x)

#==================================================================

def exercises(request):
    x = {}
    x['exercises'] = Exercise.objects.all().order_by('name')
    return render(request, 'main/exercises.html', x)
    
def add_exercise(request):
    if request.method == "POST":
        
        n = request.POST.get('name')
        
        f = request.POST.get('exercise_focus')
        
        laps = True if request.POST.get('laps') == "on" else False
        miles = True if request.POST.get('miles') == "on" else False
        reps = True if request.POST.get('reps') == "on" else False
        sets = True if request.POST.get('sets') == "on" else False
        time = True if request.POST.get('time') == "on" else False
        weight = True if request.POST.get('weight') == "on" else False
        
        sun = True if request.POST.get('sunday') == "on" else False
        mon = True if request.POST.get('monday') == "on" else False
        tue = True if request.POST.get('tuesday') == "on" else False
        wed = True if request.POST.get('wednesday') == "on" else False
        thu = True if request.POST.get('thursday') == "on" else False
        fri = True if request.POST.get('friday') == "on" else False
        sat = True if request.POST.get('saturday') == "on" else False
        
        Exercise.objects.create(
            name = n,
            exercise_focus = ExerciseFocus.objects.get(
                name = f),
            laps = laps,
            miles = miles,
            reps = reps,
            sets = sets,
            time = time,
            weight = weight,
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
        x['exercise_focuses'] = ExerciseFocus.objects.all()
        x['cardio_types'] = CardioType.objects.all()
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
        
def exercise_detail(request, pk):
    certain_exercise = Exercise.objects.get(
            id = pk)
    
    chart_data = []
    chart_data += [['Date','Weight']]
    
    certain_exercise_data = ExerciseEntry.objects.filter(
        exercise = certain_exercise).order_by('date')
    
    for entry in certain_exercise_data:
        chart_data += [[entry.date.strftime('%m/%d/%Y'),entry.weight]]
    
    if len(certain_exercise_data) is 0:
        chart_empty = True
    else:
        chart_empty = False
    
    x = {}
    x['chart_empty'] = chart_empty
    x['certain_exercise'] = Exercise.objects.get(pk=pk)
    x['chart_data'] = chart_data
    x['chart_title'] = certain_exercise.name
    x['chart_x_axis_label'] = chart_data[0][0]
    return render(request, 'main/exercise_detail.html', x)

#==================================================================
    
def exercise_entries(request):
    
    
    x = {}
    x['exercise_entries'] = ExerciseEntry.objects.all()
    # x['output'] = column2d.render()
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
