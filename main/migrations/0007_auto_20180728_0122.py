# Generated by Django 2.0.3 on 2018-07-28 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180727_0201'),
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