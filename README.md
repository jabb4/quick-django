# Quickly deploy a django-docker instanse.
Just run `docker compose build` and `docker compose up` to get your django website running
Edit in .env to wanted values. Befor deploying make sure all secrets and passwords are changed in .env file.
To create a new "app" in django use the createapp.py script and make sure to be in the app directory. Use the script this way: `python createapp.py <app_name>`


To run a function in the background (with celery) use the tasks.py. This is usefull if the backend need to do processing and you want the frontend to load still.

If you need to run schedual tasks look in to django_celery_beat (not implemented)

How to create a superuser:
´´´
docker exec -it django python manage.py createsuperuser
´´´

To start docker:
´´´
docker compose up -d
´´´

To stop docker:
´´´
docker compose down
´´´

To stop docker and clear db:
´´´
docker compose down -v
´´´