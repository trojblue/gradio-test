
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

from celery import Celery

app = Celery('tasks', broker='amqp://yada:TempPassMQ0@54.160.137.8/myvhost',
             backend='rpc://')
@app.task
def add(x, y):
    return (x + y)*2