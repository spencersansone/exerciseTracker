from django.db import models

class ExerciseFocus(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    exercise_focus = models.ForeignKey(ExerciseFocus, on_delete=models.CASCADE)
    weight_involved = models.BooleanField()
    
    sunday = models.BooleanField()
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    
    def __str__(self):
        return self.name
    
class ExerciseEntry(models.Model):
    date = models.DateField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.FloatField(blank=True,null=True)
    

# Create your models here.
