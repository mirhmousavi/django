import os

errorlog = '-'
accesslog = '-'
capture_output = True

bind = ['0.0.0.0:5000']

workers = os.getenv('GUNICORN_WORKERS')
worker_class = os.getenv('GUNICORN_WORKER_CLASS')
