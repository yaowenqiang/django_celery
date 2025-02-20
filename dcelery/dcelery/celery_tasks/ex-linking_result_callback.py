from dcelery.celery import app
import sys
from time import sleep

@app.task(queue='tasks')
def long_running_task():
    raise ValueError('An error occurred')

@app.task(queue='tasks')
def process_task_result(result):
    sys.stdout.write(f'Processing task result: {result}\n')
    sys.stdout.flush()

@app.task(queue='tasks')
def error_handle(task_id, exc, traceback):
    sys.stdout.write('>>>')
    sys.stdout.write(str(exc))
    sys.stdout.write('>>>')
    sys.stdout.flush()

def run_task():
    long_running_task.apply_sync(link=[process_task_result.s(),], link_error=[process_task_result.s()])
