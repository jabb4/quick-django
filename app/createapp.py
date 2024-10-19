import sys
import subprocess
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: python createapp.py 'app name'")
    exit()
elif Path("manage.py").is_file():
    app_name = sys.argv[1]
else:
    print("you need to be in root directory to create an app")
    exit()

## Creating new app
startapp_process = subprocess.run(["python","manage.py", "startapp", app_name])
if startapp_process.returncode == 1:
    exit()

### Add new app to settings
with open("app/settings.py", "r") as file:
   settings = file.readlines()
   for line in enumerate(settings):
       if "INSTALLED_APPS = [\n" == line[1]:
        settings.insert(line[0]+1,f'    "{app_name}",\n')
        with open("app/settings.py", "w") as file:
            file.write("")
            file.writelines(settings)

## Create templates dir
if not Path(f"{app_name}/templates").exists():
    Path(f"{app_name}/templates").mkdir()

## Create tasks.py file
with open(f"{app_name}/tasks.py", "w") as file:
   file.writelines([
       "from celery import shared_task\n",
       "# from time import sleep\n",
       "\n",
       "# Example for function to do in background",
       '# @shared_task(bind=True)\n',
       "# def example_task(self):\n",
       "#     print(self.request.id)\n",
       "#     for i in range(1,101):",
       "#        print(i)\n",
       "#        self.update_state(state='PROGRESS', meta={'current': i, 'total': 100})\n",
       "#        sleep(1)\n",
       '#     return "Done"\n',
    ])

## Create urls.py file
with open(f"{app_name}/urls.py", "w") as file:
   file.writelines(["from django.urls import path\n", "from . import views\n", "\n", "urlpatterns = [\n", "\n", "]"])

## Config base urls file
with open("app/urls.py", "r") as file:
    urls = file.readlines()
    for line in enumerate(urls):
        if "urlpatterns = [\n" == line[1]:
            urls.insert(line[0]+1,f'    path("{app_name}/", include("{app_name}.urls")),\n')
            with open("app/urls.py", "w") as file:
                file.write("")
                file.writelines(urls)