# Generated by Django 2.0.3 on 2018-08-01 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20180801_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weight', models.FloatField(blank=True, null=True)),
                ('miles', models.FloatField(blank=True, null=True)),
                ('time', models.DurationField(blank=True, null=True)),
                ('laps', models.IntegerField(blank=True, null=True)),
                ('reps', models.IntegerField(blank=True, null=True)),
                ('sets', models.IntegerField(blank=True, null=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Exercise')),
            ],
        ),
    ]
