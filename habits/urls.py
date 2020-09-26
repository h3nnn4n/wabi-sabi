from django.urls import path

from . import views

# pylint: disable=invalid-name
app_name = 'habits'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<uuid:pk>/', views.HabitView.as_view(), name='detail'),
    path('new/', views.HabitNewView.as_view(), name='new_habit'),
    path('create/', views.create_habit, name='create_habit'),
]
