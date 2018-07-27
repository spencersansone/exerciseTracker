from . import views
from django.conf.urls import url

app_name = 'main'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^exercises/$', views.exercises, name='exercises'),
    url(r'^add_exercise/$', views.add_exercise, name='add_exercise'),
    url(r'^exercise_entries/$', views.exercise_entries, name='exercise_entries'),
    url(r'^add_exercise_entry/$', views.add_exercise_entry, name='add_exercise_entry'),
    url(r'^add_focus/$', views.add_focus, name='add_focus'),
    url(r'^delete_focus/(?P<pk>[0-9]+)/$', views.delete_focus, name='delete_focus'),
    url(r'^delete_exercise/(?P<pk>[0-9]+)/$', views.delete_exercise, name='delete_exercise'),
    url(r'^focuses/$', views.focuses, name='focuses'),
]