from django.db import models

class ExerciseFocus(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CardioType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    exercise_focus = models.ForeignKey(ExerciseFocus, on_delete=models.CASCADE)
    weight_involved = models.BooleanField()
    
    is_cardio = models.BooleanField()
    cardio_type = models.ForeignKey(CardioType, on_delete=models.CASCADE, blank=True, null=True)
    
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
    weight = models.FloatField(blank=True, null=True)
    
    miles = models.FloatField(blank=True, null=True)
    time = models.DurationField(blank=True, null=True)
    laps = models.IntegerField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    sets = models.IntegerField(blank=True, null=True)
    

# Create your models here.
