import os
import time

from dcelery.dcelery.celery_config import Celery
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

app = Celery('celery')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.task_que = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks', queue_arguments={'x-max-priority': 10}),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1


base_dir = os.getcwd()

task_folder = os.path.join(base_dir, 'dcelery', 'celery_tasks')

if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for file in os.listdir(task_folder):
        if file.startswith('ex') and file.endswith('.py'):
            module_name = f"{dcelery.celery_tasks}.{file[:-3]}"
            module = __import__(module_name, fromlist=['*'])

            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj) and name.startswith('my_tasks'):
                    task_modules.append(f'{module_name}.{name}')
    
app.autodiscover_tasks(task_modules)

