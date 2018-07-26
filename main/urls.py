from . import views
from django.conf.urls import url

app_name = 'main'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^exercises/$', views.exercises, name='exercises'),
    url(r'^add_exercise/$', views.add_exercise, name='add_exercise'),
    url(r'^exercise_entries/$', views.exercise_entries, name='exercise_entries'),
]