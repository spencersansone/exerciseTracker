# Generated by Django 2.0.3 on 2018-08-01 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20180728_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='focus',
        ),
        migrations.RemoveField(
            model_name='exerciseentry',
            name='exercise',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='ExerciseEntry',
        ),
        migrations.DeleteModel(
            name='Focus',
        ),
    ]
