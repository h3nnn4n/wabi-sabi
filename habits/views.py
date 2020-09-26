from django.views import generic

from .models import Habit, Event, User


class IndexView(generic.ListView):
    template_name = 'habits/index.html'
    context_object_name = 'latest_habits_list'

    def get_queryset(self):
        """
        Returns the most recently created habits
        """
        return Habit.objects.order_by('-created_at')[:5]


class HabitView(generic.DetailView):
    model = Habit
    template_name = 'habits/habit_detail.html'
