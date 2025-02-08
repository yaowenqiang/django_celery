from celery import shared_task
import time
@shared_task
def sharedtask():
    return

@shared_task
def task1():
    return

@shared_task
def task2():
    return

@shared_task
def task3(queue='celery'):
    time.sleep(10)
    return
@shared_task
def task4(queue='celery:1'):
    time.sleep(10)
    return
@shared_task
def task5(queue='celery:2'):
    time.sleep(10)
    return
@shared_task
def task6(queue='celery:3', task_rate_limit='10/m'):
    time.sleep(10)
    return