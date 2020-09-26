from django.views import generic

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
