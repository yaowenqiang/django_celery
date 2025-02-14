from dcelery.celery_config import app
import logging

logging.basicConfig(filename='celery.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')



@app.task(queue='tasks'):
def my_task():
    pass

@app.task(queue='tasks'):
def my_task2():
    try:
        raise ConnectionError('Connection Error')
    except ConnectionError as e:
        logging.error(e)
        raise ConnectionError()