    

# Celery Tasks

+ Asynchronous Task Execution
+ Distributed Task Queue
+ Task Scheduling and Perodic Tasks
+ Result Handling
+ Error handling and Retry Mechanism
+ Monitoring and Management

## Preparing a Docker Working Environment for Django

> pip install django
> pip install celery
> pip install redis

> django-admin startproject dcelery

> docker compose up -d --build

http://localhost:8001/

> docker exec -it django /bin/sh

> ./manage.py startapp newapp

> ./manage.py shell

> from newapp.tasks import sharedtask
> sharedtask.delay()

## Types of Scheduling Mechanisums:

+ Time-based Scheduling
+ Event-based Scheduling
+ Dependency-based Scheduling

## Benefits of Automated Task Scheduling:

+ Increased Effenciency
+ Optimal Resourced Utilization
+ Improved Scalability
+ Enhanced Reliability

## Task Routing


+ Efficient and lntelligent distribution of tasks
+ Process of determining the destination of tasks
+ Allows you to control how tasks are dispatched to worker nodes
+ Improved Scalability
+ Load Balancing
+ Granular Control

### Advanced Routing Techniques:

+ Dynamic Routing based on Runtime Conditions
+ Routing based on task Arguments or context
+ Using External routing Strategies or Plugins

## Prioritize Tasks

+ Ensure critial tasks are executed first
+ Optimize resource utilization
+ Meet SLAs and deadlines
+ handle high-priority or time-sensitive requests efficiently

### Setting Task Priority:

+ 0 and 9 (0 being the lowest priority and 9 being the highest)
+ Default specified in the task decorator or configuration

### Configuring Worker Queues

+ Define multiple queues representing different priorities
+ Associate each queue with a specific priority level
+ Celery worker consumes tasks from queues based on their priority


## Task Grouping

```python

from celery import group

from newtasks import tp1, tp2,tp3, tp4
tasks_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
tasks_group.apply_async()
```

## Task Chaining



```python
from celery import chain
from newtasks import tp1, tp2,tp3, tp4
tasks_chain = chain(tp1.s(), tp2.s(), tp3.s(), tp4.s())
tasks_chain.apply_async()
```

## Task Rate limites


> pip install pika
>
> docker stop $(docker ps -aq) && docker rm $(docker ps -aq) && docker rmi $(docker images -q) && docker volume prune -f && docker network prune -f


```python
from dcelery.celery import t1, t2,t3

t1.apply_async(priority=5)
t1.apply_async(priority=6)
t1.apply_async(priority=7)
t1.apply_async(priority=9)

```

> celery inspect active
> celery inspect active_queues

## Passing arguments and returning results from Celery tasks


```python
    from dcelery.tasks import t1
    result = t1.apply_async(args=[1,2,3], kwargs={'a':1, 'b':2})
    print(result.get())
```

### AsyncResult

+ isComplete(): Checks whether the task associated with the AsyncResult object has completed
+ isSuccessful(): Checks whether the task completed successfully
+ get(): Blocks the current thread until the task compeletes
+ getResult(): Returns if task has completed succeffully
+ getException(): Returns the exception or error
+ ready(): 

## Executing tasks synchronously and asynchronously

+ Synchronous execution: Tasks are executed immediately in the same thread
+ Asynchronous execution: Tasks are executed in a separate thread or process

## Task Retry Mechanism

+ Retry failed tasks automatically
+ Retry failed tasks after a specified delay
+ Retry failed tasks a specified number of times
+ Retry failed tasks based on specific conditions

## Task Retry Policies

## Celery Flower

### Purpose of Celery Flower

+ Monitoring
+ Management
+ Visualization

## Common Types of Exceptions and Errors in Celery Tasks

### Network Errors

+ Connection timeout
+ DNS resolution failure
+ Network connectivity issues

### Database Connection Issues

+ Database server unavailability
+ Authentication errors
+ Connection pool exhaustion


### External Service Failures

### Custom Application-Specific Errors

## Dead-letter Queues


## Task Signals Graceful shutdown and Cleanup of Failed Tasks

### Common events

+ task_prerun: Triggered before a task starts executing
+ task_postrun: Triggered rigit after a task finishes executing,regardless of success or failure
+ task_success: Triggered when a task completes successfully
+ task_failure: Triggered when a task fails or raises an exception
+ task_revoked: Triggered when a task is manually revoked
+ task_retry: Triggered when a task is retried


## Error Tracking and Monitoring with Sentry

> https://sentry.io/

> pip install --upgrade 'sentry-sdk[django]'


## Task Scheduling

+ Orchestrating the execution
+ Automate routine process

### Type of Scheduling Machanisms

+ Time-based Scheduling
+ Event-based Scheduling
+ Dependency-based Scheduling


### Benifits of Automated Task Scheduling

+ Increased Efficiency
+ Optimal Resource Utilization
+ Improved Schalability
+ Enhanced Reliability


### Understanding Periodic Tasks

+ Time based recurring tasks


### Configuring Celery for Periodic Tasks

+ Celery beat scheduler configuration
+ Deining Periodic Tasks
+ Customizing Periodic Task


### Build Crontab Schedules

```python
from celery.schedules import crontab

app.conf.beat_schedule = {
    'task1': {
        'task': 'tasks.task1',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
    },
    'task2': {
        'task': 'tasks.task2',
        'schedule': crontab(hour=8, minute=0),
    },
}
```

### Celery Beat Configuration

+ CELERY_BEAT_SCHEDULE
+ CELERY_BEAT_SCHEDULE_FILENAME
+ CELERY_BEAT_SCHEDULE_MAX_ACTIVE
```

### Django Celery beat

> pip install django-celery-beat

## Monitoring Service Status Including Custom Event Tracking and Alerting


```
# docker-compose.yml

env_file:
    - ./.env
```


```python
from sentry import capture_exception

try:
    # Code that may raise an exception
except Exception as e:
    capture_exception(e)

```