
"""
celery --app=dcelery worker -l INFO -Q tasks -E -B
B for beat
E for events
"""

from datetime import datetime, timedelta
from dcelery.celery_config import app

app.conf.beat_schedule = {
    'task1': {
        'task': dcelery.celery_tasks.ex_task_scheduling.task1,
        'schedule': timedelta(seconds=5),
    },
    'task2': {
        'task': dcelery.celery_tasks.ex_task_scheduling.task2,
        'schedule': timedelta(seconds=10),
    },
    'task3': {
        'task': dcelery.celery_tasks.ex_task_scheduling.task2,
        'schedule': timedelta(seconds=10),
        "kwargs":{"foo":"bar"},
        "args":(1,2,3),
        "options": {"queue": "tasks"},
        "priority": 10,
    },
}

@app.task
def task1(queue='tasks'):
    print('Running task 1')

@app.task
def task2(queue='tasks'):
    print('Running task 2')