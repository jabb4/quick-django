# Quickly deploy a django-docker instanse.
Just run `docker compose build` and `docker compose up` to get your django website running
Edit in .env to wanted values. Befor deploying make sure all secrets and passwords are changed in .env file.
To create a new "app" in django use the createapp.py script and make sure to be in the app directory. Use the script this way: `python createapp.py <app_name>`
