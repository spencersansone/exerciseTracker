from . import views
from django.conf.urls import url

app_name = 'main'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^exercises/$', views.exercises, name='exercises'),
    url(r'^add_exercise/$', views.add_exercise, name='add_exercise'),
    url(r'^exercise_entries/$', views.exercise_entries, name='exercise_entries'),
    url(r'^add_exercise_entry/(?P<pk>[0-9]+)/$', views.add_exercise_entry, name='add_exercise_entry'),
    url(r'^add_exercise_focus/$', views.add_exercise_focus, name='add_exercise_focus'),
    url(r'^delete_exercise_focus/(?P<pk>[0-9]+)/$', views.delete_exercise_focus, name='delete_exercise_focus'),
    url(r'^delete_exercise/(?P<pk>[0-9]+)/$', views.delete_exercise, name='delete_exercise'),
    url(r'^exercise_focuses/$', views.exercise_focuses, name='exercise_focuses'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^today/$', views.today, name='today'),
    url(r'^exercise_detail/(?P<pk>[0-9]+)/$', views.exercise_detail, name='exercise_detail'),
    url(r'^help/$', views.help, name='help'),
    url(r'^routine/$', views.routine, name='routine'),
]