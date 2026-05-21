release: python JokesProject/manage.py migrate && python JokesProject/manage.py collectstatic --noinput
web: gunicorn JokesProject.JokesProject.wsgi:application --bind 0.0.0.0:$PORT

