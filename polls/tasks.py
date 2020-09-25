import random

from celery import shared_task
from django.db.models import F

from .models import Choice


@shared_task
def random_vote_task():
    if Choice.objects.count() == 0:
        return

    try:
        max_id = Choice.objects.order_by('-id')[0].id
        random_id = random.randint(0, max_id)
        choice = Choice.objects.filter(id__gte=random_id)[0]

        choice.votes = F('votes') + 1
        choice.save()
    except IndexError:
        pass
