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

class CardioTypeList(admin.ModelAdmin):
    list_display = ('id',)
    ordering = ['id']

admin.site.register(CardioType, CardioTypeList)
# Register your models here.
