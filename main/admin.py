from django.contrib import admin
from .models import *

class FocusList(admin.ModelAdmin):
    list_display = ('id',)
    ordering = ['id']

admin.site.register(Focus, FocusList)

class ExerciseList(admin.ModelAdmin):
    list_display = ('id',)
    ordering = ['id']

admin.site.register(Exercise, ExerciseList)

class ExerciseEntryList(admin.ModelAdmin):
    list_display = ('id',)
    ordering = ['id']

admin.site.register(ExerciseEntry, ExerciseEntryList)
# Register your models here.
