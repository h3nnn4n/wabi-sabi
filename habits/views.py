from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

# pylint: disable=no-name-in-module
from psycopg2.errors import NotNullViolation

from .models import Habit
from .forms import EventForm


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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            habit = Habit.objects.get(pk=kwargs['pk'])
            if not habit.public:
                return redirect('habits:index')

        # Not sure if this is a good idea or not
        return super().dispatch(request)


class HabitNewView(generic.CreateView):
    model = Habit
    template_name = 'habits/habit_new.html'
    fields = [
        'name',
        'public',
    ]

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('habits:index')

        # Not sure if this is a good idea or not
        return super().dispatch(request)


def create_habit(request):
    habit = None

    try:
        habit = Habit(user=request.user)
        habit.name = request.POST['name']
        habit.public = request.POST.get('public', 'off') == 'on'
        habit.created_at = timezone.now()
        habit.save()
    except (NotNullViolation, KeyError):
        return render(request, 'habits/habit_new.html', {
            'habit': habit,
            'error_message': 'Error while creating Habit',
        })
    else:
        return HttpResponseRedirect(reverse('habits:detail', args=(habit.id,)))


def new_event(request, habit_id):
    if not request.user.is_authenticated:
        habit = Habit.objects.get(pk=habit_id)

        if habit.public:
            return redirect('habits:detail', pk=habit_id)
        else:
            return redirect('habits:index')

    habit = Habit.objects.get(pk=habit_id)

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.habit = habit
            event.created_at = timezone.now()
            event.save()

            return redirect('habits:detail', pk=habit_id)
    else:
        form = EventForm()

    return render(request, 'habits/new_event.html', {'form': form, 'habit': habit})
