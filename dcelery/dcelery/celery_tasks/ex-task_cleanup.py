# celery --app=dcelery -l INFO -Q tasks, dead_letter -E

from celery.signals import task_failure
from dcelery.celery_config import app
import sys

@app.task(queue='tasks')
def clear_failed_task(task_id):
    sys.stdout.write(f"Clearing failed task {task_id}\n")

@app.task(queue='tasks')
def my_task():
    raise ValueError("This task failed")

@task_failure.connect(sender=my_task)
def task_failure_handler(sender=None, task_id=None, **kwargs):
    clear_failed_task.delay(task_id)

def run_task():
    my_task.apply_async()