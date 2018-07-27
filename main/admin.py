from django.contrib import admin
from .models import *

class FocusList(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ['id']

admin.site.register(Focus, FocusList)

class ExerciseList(admin.ModelAdmin):
    list_display = ('name','focus','weight_involved',)
    ordering = ['id']

admin.site.register(Exercise, ExerciseList)

class ExerciseEntryList(admin.ModelAdmin):
    list_display = ('date','exercise','weight',)
    ordering = ['id']

admin.site.register(ExerciseEntry, ExerciseEntryList)
# Register your models here.
