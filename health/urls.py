from django.urls import path
from . import views

# pylint: disable=invalid-name
app_name = 'health'
urlpatterns = [
    path('', views.index, name='index'),
]
