from . import views
from django.conf.urls import url

app_name = 'NAMEOFAPPHERE!'

urlpatterns = [
    url(r'^$', views.home, name='home'),
]