import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()


class Habit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()

    def __str__(self):
        return str(self.name)

    def events(self):
        return self.event_set.all()


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, null=False, blank=False)
    notes = models.CharField(max_length=1024, blank=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.habit.name}: {self.notes or "n/a"}'
