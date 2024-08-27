# PokerStatsData

[**PokerStatsData**](http://193.187.175.182:1337) is a web application for converting and organizing poker session statistics in a dictionary-like
manner (key-value pairs).

The application receives poker session data separated by a certain separator (space, by default). As a result, the
application produces this data connected to the corresponding keys.

You can try the application [here](http://193.187.175.182:1337).
___

## Technologies

[![Python](https://img.shields.io/badge/Python-3.10-%23FFD040?logo=python&logoColor=white&labelColor=%23376E9D)](https://www.python.org/downloads/release/python-31012/)
[![Django](https://img.shields.io/badge/Django-4.1-%232BA977?logo=django&logoColor=white&labelColor=%23092E20)](https://www.djangoproject.com/)

[![Gunicorn](https://img.shields.io/badge/Gunicorn-%23479946?logo=gunicorn&logoColor=white&labelColor=%23293133)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/Nginx-%23009639?logo=nginx&logoColor=white&labelColor=%23293133)](https://nginx.org/)

[![HTML](https://img.shields.io/badge/HTML-%23E44D25?logoColor=white&labelColor=%23293133&logo=html5)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-%23214CE5?logoColor=white&labelColor=%23293133&logo=css3)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-%23FFD83A?logoColor=white&labelColor=%23293133&logo=javascript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%232F6792?logoColor=white&labelColor=%23293133&logo=postgresql)](https://www.postgresql.org/)
[![SQLite](https://img.shields.io/badge/SQLite-%23003156?logoColor=white&labelColor=%23293133&logo=sqlite)](https://www.sqlite.org/)

[![Docker](https://img.shields.io/badge/Docker-%232496ED?logo=docker&logoColor=white&labelColor=%23293133)](https://www.docker.com/)

[![GitHub](https://img.shields.io/badge/GitHub-%23000000?logoColor=white&labelColor=%23293133&logo=github)](https://github.com/)

___

## Installation

Run the following commands to bootstrap your environment.

For Windows:

```commandline
git clone https://github.com/rYauheni/PokerStatsData.git

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

copy .env.template .env

```

For Linux:

```commandline
git clone https://github.com/rYauheni/PokerStatsData.git

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

cp .env.template .env
```

___

## QuickStart for development

1. Determine the value of environment variables in the file `.env`


2. Run the app locally:
   
   for Windows:

   ```commandline
   python manage.py runserver 0.0.0.0:8000 --settings=poker_stats_data.settings.dev
   ```
   
   for Linux:

   ```commandline
   python3 manage.py runserver 0.0.0.0:8000 --settings=poker_stats_data.settings.dev
   ```
   
3. Run the app with gunicorn:

   for Windows&Linux:
   ```commandline
   gunicorn poker_stats_data.wsgi:application --bind 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=poker_stats_data.settings.dev
   ```

4. Apply migrations:

   for Windows:

    ```commandline
    python manage.py migrate --settings=poker_stats_data.settings.dev
    ```

   for Linux:

   ```commandline
   python3 manage.py migrate --settings=poker_stats_data.settings.dev
   ```

5. Run tests:

   for Windows:

    ```commandline
    python manage.py test  --settings=poker_stats_data.settings.dev
    ```

   for Linux:

   ```commandline
   python3 manage.py test  --settings=poker_stats_data.settings.dev
   ```
___

## Launch for production

1. Determine the value of environment variables in the file `.env`


2. Add your server IP address to `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` in `/poker_stats_data/settings/base.py/`.


3. Run docker container with command:

    ```commandline
    docker compose up
    ```

4. Apply migrations:

    ```commandline
    docker compose exec web python manage.py migrate --noinput --settings=poker_stats_data.settings.prod
    ```

5. Create superuser

    ```commandline
    docker compose exec web python manage.py createsuperuser --settings=poker_stats_data.settings.prod
    ```

 ___

## Contributing

Bug reports and/or pull requests are welcome
___

## License

The app is dedicated to the public domain under the CC0 license