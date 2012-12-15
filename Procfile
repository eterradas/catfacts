web: python manage.py run_gunicorn --settings=catfacts.settings.heroku
celeryd: python manage.py celeryd -E -B --loglevel=INFO syncdb --settings=catfacts.settings.heroku
