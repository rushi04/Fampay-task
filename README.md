# Fampay-task



### Run Locally

- Django server
- Celery Worker
- redis-server 

```
cd Fampay
python3 manage.py makemigrations
python3 manage.py migrate
```

**Start Redis Server**

`redis-server`

**Celery Worker**

`celery -A Fampay worker --beat -S django -l info`

**Start Django Server**

`python3 manage.py runserver`
