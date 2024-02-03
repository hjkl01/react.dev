# django

### load environment

```python
# load environment
import os
envs = os.environ
for k, v in envs.items():
    print(k, v)

# load .env
# pip install django-environ

import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=True)

from django.core.management.utils import get_random_secret_key
SECRET_KEY = env("SECRET_KEY", default=get_random_secret_key())

# database url https://pypi.org/project/dj-database-url/
# pip install dj_database_url

import dj_database_url
# write .env and set DATABASE_URL
DATABASES = {
    "default": dj_database_url.config(
        default=env("DATABASE_URL", default="sqlite:///db.sqlite3"), conn_max_age=600, conn_health_checks=True
    )
}
```

### auto load app

```python
# mkdir -p apps/appname
# django-admin startapp appname apps/appname
# update apps/appname/apps.py
name = "apps.appname"

# settings.py
APPS_FLODER = os.path.join(BASE_DIR, "apps")
APPS = [_ for _ in os.listdir(APPS_FLODER) if os.path.isdir(os.path.join(APPS_FLODER, _)) and "pycache" not in _]
INSTALLED_APPS += ["apps." + _ for _ in APPS]
```

### cors

```python
# pip install django-cors-headers

INSTALLED_APPS = (
    ...
    'corsheaders',
    ...
)

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS=True

# Load the default ones
CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]
```

### static in debug mode

```python
python manage.py runserver 0.0.0.0:8000 --insecure
```

### dump and load data

```shell
python manage.py dumpdata (myapp) > myapp.json

python manage.py loaddata myapp.json
```

### save data with scripts

```python
import os
import django
from proxyip.models import ProxyIP

os.environ['DJANGO_SETTINGS_MODULE'] = 'dj_project.settings'
django.setup()

p = ProxyIP(ip='192.168.50.1')
p.save()
print(ProxyIP.objects.all())

python manage.py shell < main.py
```
