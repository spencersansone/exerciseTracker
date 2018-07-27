from django.db import models

class Focus(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    focus = models.ForeignKey(Focus, on_delete=models.CASCADE)
    weight_involved = models.BooleanField()
    
    def __str__(self):
        return self.name
    
class ExerciseEntry(models.Model):
    date = models.DateField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.FloatField(blank=True,null=True)
    

# Create your models here.
