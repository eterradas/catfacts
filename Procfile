web: python manage.py run_gunicorn --settings=settings.heroku
celeryd: python manage.py celeryd -E -B --loglevel=INFO syncdb --settings=settings.heroku
