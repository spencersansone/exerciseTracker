# Generated by Django 2.0.3 on 2018-07-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180726_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseentry',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
