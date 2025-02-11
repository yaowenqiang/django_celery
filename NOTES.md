    

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


