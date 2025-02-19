import os
from celery import Celery, group
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

app = Celery('dcelery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks', queue_arguments={'x-max-priority': 10}),
    Queue('dead_letter', routing_key='dead_letter'),
]

app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

base_dir = os.getcwd()
task_folder = os.path.join(base_dir, 'dcelery', 'celery_tasks')

if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for file in os.listdir(task_folder):
        if file.startswith('ex') and file.endswith('.py'):
            module_name = f"dcelery.celery_tasks.{file[:-3]}"
            module = __import__(module_name, fromlist=['*'])

            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj) and name.startswith('my_task'):
                    task_modules.append(f'{module_name}.{name}')

@app.task(queue='tasks')
def my_task(z):
    try:
        if z == 3:
            raise ValueError("Number is invalid")
    except Exception as e:
        handle_failed_task.apply_async(args=(z, str(e)))

@app.task(queue='dead_letter')
def handle_failed_task(z, error_message):
    return f"Task failed with value {z} and error {error_message}"

def run_task_group():
    task_group = group(
        my_task.s(i) for i in range(5)
    )
    task_group.apply_async()
