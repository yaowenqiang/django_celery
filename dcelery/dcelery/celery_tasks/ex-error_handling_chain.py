from celery import chain
from dcelery.celery_config import app


@app.task(queue='tasks')
def add(x, y):
    return x + y


@app.task(queue='tasks')
def multiply(result):
    if result == 0:
        raise ValueError("Number is invalid")
    return result * 2


def run_task_chain():
    task_chain = chain(add.s(1, 2), multiply.s(0))
    result = task_chain.apply_async()
    result.get()