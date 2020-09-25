import random

from celery import shared_task
from django.db.models import F

from .models import Choice


@shared_task
def random_vote_task():
    if Choice.objects.count() == 0:
        return -1

    try:
        max_id = Choice.objects.order_by('-id')[0].id
        random_id = random.randint(1, max_id + 1)
        choice = Choice.objects.filter(id__gte=random_id)[0]

        choice.votes = F('votes') + 1
        choice.save()
    except IndexError:
        print('invalid index')
        return -1

    return choice.id
