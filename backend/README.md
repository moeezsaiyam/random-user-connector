# backend

## Important Files

-   `connector_api/tasks.py` [The function that get data from api and save in db perodically]
-   `connector_api/views.py` [The User API backend]
-   `connector_api/models.py` [The User Model]
-   `conf/celery.py` [Celery Setup For tasks scheduling]
-   `conf/settings.py` [Configurations File]

## Steps to run backend locally (without Docker)

-   `pip install -r requirements.txt` [Install the required packages]
-   `python manage.py makemigrations` [Make migrations of models]
-   `python manage.py migrate` [Migrate the migrations to DB]
-   `python manage.py runserver` [Start the backend Server]

### To Run Celery and Redis for Task Scheduling
-   Install Redis from https://redis.io/docs/getting-started/ [depending upon your system] and Run Redis Server using `redis-server` command
-   Run Celery using `celery -A conf.celery worker -B -l info` command