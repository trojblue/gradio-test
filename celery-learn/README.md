
启动client:
```bash
celery -A tasks worker --loglevel=INFO
```



并行:
```python
from celery import group
from tasks import add

if __name__ == '__main__':
    tasks_list = [add.s(4, 4), add.s(5, 5), add.s(6, 6)]
    tasks_group = group(tasks_list)
    tasks_result = tasks_group.apply_async()
    results = tasks_result.join()
    print(results)
```


设置限制(并行数, 启动时):
```bash
celery -A your_project.celery worker --loglevel=info --concurrency=1
```