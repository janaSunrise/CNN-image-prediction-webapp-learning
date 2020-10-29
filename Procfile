release: python manage.py makemigrations cnn && python manage.py migrate
web: gunicorn django_mobilenet.wsgi --log-file - 
