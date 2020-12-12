# Fampay-task



### Run Locally

- Django server
- Celery Worker
- redis-server 

```
cd fampay
python3 manage.py makemigrations
python3 manage.py migrate
```

**Start Redis Server**

`redis-server`

**Celery Worker**

`celery -A fampay worker --beat -S django -l info`

**Start Django Server**

`python3 manage.py runserver`