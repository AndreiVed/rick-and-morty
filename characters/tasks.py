from celery import shared_task

from characters.models import Character


@shared_task
def count_characters() -> int:
    return Character.objects.count()
