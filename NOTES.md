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
