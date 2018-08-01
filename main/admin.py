from django.contrib import admin
from .models import *

class ExerciseFocusList(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ['id']

admin.site.register(ExerciseFocus, ExerciseFocusList)

class ExerciseList(admin.ModelAdmin):
    list_display = ('name','exercise_focus','weight_involved','sunday','monday','tuesday','wednesday','thursday','friday','saturday',)
    ordering = ['id']

admin.site.register(Exercise, ExerciseList)

class ExerciseEntryList(admin.ModelAdmin):
    list_display = ('date','exercise','weight',)
    ordering = ['id']

admin.site.register(ExerciseEntry, ExerciseEntryList)
# Register your models here.
