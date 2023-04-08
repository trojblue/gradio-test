from some_pkg.add import add_alt

from celery import Celery
import platform
import os

if platform.system() == 'Windows':
    # fix "ValueError: not enough values to unpack (expected 3, got 0)" on Windows
    os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')



app = Celery('tasks', broker='amqp://yada:TempPassMQ0@54.160.137.8/myvhost',
             backend='rpc://')

@app.task
def add(x, y):
    return add_alt(x, y)