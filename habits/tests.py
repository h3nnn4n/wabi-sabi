from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Habit, Event


class HabitTests(TestCase):

    def test_events_relation(self):
        user = User(first_name='test', last_name='user', email='test@user.com')
        user.save()

        habit = Habit(user=user, name='testing habit', created_at=timezone.now())
        habit.save()

        Event(habit=habit, created_at=timezone.now()).save()
        Event(habit=habit, created_at=timezone.now()).save()
        Event(habit=habit, created_at=timezone.now()).save()

        self.assertTrue(len(habit.events()) == 3)


class HabitViewTests(TestCase):
    def setUp(self):
        user1 = User(username='test user', email='test@user.com')
        user1.save()

        habit = Habit(user=user1, name='testing habit', created_at=timezone.now())
        habit.save()

        habit_public = Habit(user=user1, name='public habit', created_at=timezone.now(), public=True)
        habit_public.save()

        Event(habit=habit, created_at=timezone.now()).save()
        Event(habit=habit_public, created_at=timezone.now()).save()

        user2 = User(username='ninja user', email='ninja@japan.com')
        user2.save()

        habit = Habit(user=user2, name='private ninja secret training', created_at=timezone.now())
        habit.save()

        habit_public = Habit(user=user2, name='ninja jokes', created_at=timezone.now(), public=True)
        habit_public.save()

        Event(habit=habit, created_at=timezone.now()).save()
        Event(habit=habit_public, created_at=timezone.now()).save()

    def test_public_habits(self):
        """
        Check that only public habits are visible when no user is logged in
        """
        response = self.client.get(reverse('habits:index'))

        self.assertQuerysetEqual(
            response.context['latest_habits_list'],
            [
                '<Habit: ninja jokes>',
                '<Habit: public habit>',
            ]
        )

    def test_user_habits(self):
        """
        Check that when a user logs in, only his own habits shows up
        """
        user = User.objects.get(username='ninja user')
        self.client.force_login(user)

        response = self.client.get(reverse('habits:index'))

        self.assertQuerysetEqual(
            response.context['latest_habits_list'],
            [
                '<Habit: ninja jokes>',
                '<Habit: private ninja secret training>',
            ]
        )
