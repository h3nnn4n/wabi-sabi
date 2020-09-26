from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from psycopg2.errors import NotNullViolation

from .models import Habit


class IndexView(generic.ListView):
    template_name = 'habits/index.html'
    context_object_name = 'latest_habits_list'

    def get_queryset(self):
        """
        Returns the most recently created habits
        """
        if self.request.user.is_authenticated:
            return Habit \
                    .objects \
                    .filter(user=self.request.user.id) \
                    .order_by('-created_at')

        return Habit \
                .objects \
                .filter(public=True) \
                .order_by('-created_at')[:10]


class HabitView(generic.DetailView):
    model = Habit
    template_name = 'habits/habit_detail.html'


class HabitNewView(generic.CreateView):
    model = Habit
    template_name = 'habits/habit_new.html'
    fields = [
        'name',
        'public',
    ]


def create_habit(request):
    habit = None

    try:
        habit = Habit(user=request.user)
        habit.name = request.POST['name']
        habit.public = request.POST['public'] == 'on'
        habit.created_at = timezone.now()
        habit.save()
    except (NotNullViolation, KeyError):
        return render(request, 'habits/habit_new.html', {
            'habit': habit,
            'error_message': 'Error while creating Habit',
        })
    else:
        return HttpResponseRedirect(reverse('habits:detail', args=(habit.id,)))
