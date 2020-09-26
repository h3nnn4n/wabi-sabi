from django.test import TestCase
from django.utils import timezone

from .models import User, Habit, Event


class HabitTests(TestCase):

    def test_events_relation(self):
        user = User(name='test_user', created_at=timezone.now())
        user.save()

        habit = Habit(user=user, name='testing habit', created_at=timezone.now())
        habit.save()

        Event(habit=habit, created_at=timezone.now()).save()
        Event(habit=habit, created_at=timezone.now()).save()
        Event(habit=habit, created_at=timezone.now()).save()

        self.assertTrue(len(habit.events()) == 3)
