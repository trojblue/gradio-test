import time

from some_celery_root.tasks import add
from celery import group
def add_inf():
    while True:
        result = add.apply_async(args=(4, 4))
        print(result.get())
        time.sleep(1)

def async_add_inf():
    while True:
        tasks_list = [add.s(4, 4), add.s(5, 5), add.s(6, 6)]
        tasks_group = group(tasks_list)
        tasks_result = tasks_group.apply_async()
        results = tasks_result.join()
        print(results)
        time.sleep(0.05)

if __name__ == '__main__':
    add_inf()
