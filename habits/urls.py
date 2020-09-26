from django.urls import path

from . import views

# pylint: disable=invalid-name
app_name = 'habits'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<uuid:pk>/', views.HabitView.as_view(), name='detail'),
]
