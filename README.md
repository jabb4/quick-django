## Django Stack Docker Deployment

This project is a feature-rich Django baseplate designed to serve as the foundation for web applications. The goal is to provide a streamlined, quick-to-deploy Django environment, allowing you to focus more on building your application rather than setting up the infrastructure. Over time, this project will be expanded to include additional features. Contributions are welcome!

### Stack

- **Django** – The main framework handling everything.
- **Django REST Framework** – API framework that enables serices to commincate with the webapp through API endpoints.
- **Celery** – A task queue for handling background jobs.
- **Redis** – A message broker between Celery and Django.
- **PostgreSQL** – The primary database for the Django instance.
- **Nginx** – Serves static content and acts as a reverse proxy.

### Features

- Basic user handling (login, registration, profile editing, logout).
- Custom authentication backend.
- API capabilities for easy communication with other services.
- Background task execution, offloading computation-intensive tasks while keeping the website responsive.

### Installation

1. Clone the repository.
2. Edit the `.env` file to match your desired configurations. Make sure to update all secrets and passwords before deployment.
3. Run the following command from the directory where your `docker-compose.yml` is located:

    ```bash
    docker compose up -d --build
    ```

### Useful Commands

- **Start the containers:**

    ```bash
    docker compose up -d --build
    ```

- **Stop the containers:**

    ```bash
    docker compose down
    ```

- **Stop containers and remove the database:**

    ```bash
    docker compose down -v
    ```

- **Create a superuser:**

    ```bash
    docker exec -it django python manage.py createsuperuser
    ```

- **Create a new Django app:**

    ```bash
    python createapp.py <app_name>
    ```

### API Development

To create a new API endpoint:

1. Add a new view to `views.py` using the `@api_view` decorator.
2. Register the view in `urls.py`.
3. If you are returning data from model objects, use serializers to ensure proper formatting.
4. For data modifications, use serializers to validate incoming data, and then save the object.

**Example:**

*File: viesw.py*
```python
@api_view(["GET"])
def example_get(request):
    data = ExampleModel.objects.all()
    serializer = ExampleSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def example_post(request):
    serializer = ExampleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
```

### Background Tasks

Celery enables background task processing without stalling the website.

To create a background task:

1. Add a new function in `tasks.py` and decorate it with `@shared_task(bind=True)`. This makes the function executable by Celery workers instead of the main Django instance.
2. Call the function asynchronously using `.delay()`.

To monitor task progress, retrieve the task ID using `self.request.id` inside the task function. You can store this ID and check the status by querying `django_celery_results.models.TaskResult`.

**Example:**

*File: task.py*
```python
@shared_task(bind=True)
def example_task(self):
    id = self.request.id
    # Your task logic here
    return "Task Completed"
```
*File: viesw.py*
```python
# Call this task
example_task.delay()
```