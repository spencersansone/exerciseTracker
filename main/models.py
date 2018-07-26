from django.db import models

class Focus(models.Model):
    name = models.CharField(max_length=100)

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    focus = models.ForeignKey(Focus, on_delete=models.CASCADE)
    weight = models.BooleanField()
    
class ExerciseEntry(models.Model):
    date = models.DateField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.FloatField(blank=True)
    

# Create your models here.
