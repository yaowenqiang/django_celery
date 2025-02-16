from dcelery.celery_config import app
from celery import Task
import logging

logging.basicConfig(filename='celery.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

class CustomClass(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error(einfo)
        else:
            print('{0!r} failed: {1!r}'.format(task_id, exc))

app.Task = CustomClass()

@app.task(queue='tasks')
def my_task():
    pass

@app.task(queue='tasks', auto_retry_for=(ConnectionError,), default_retry_delay=5, retry_kwargs={'max_retries': 5})
def my_task2():
    try:
        raise ConnectionError('Connection Error')
    except ConnectionError as e:
        logging.error(e)
        raise ConnectionError()