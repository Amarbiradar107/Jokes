release: cd JokesProject && python manage.py migrate && python manage.py collectstatic --noinput
web: cd JokesProject && gunicorn JokesProject.wsgi:application --bind 0.0.0.0:$PORT

