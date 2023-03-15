import os

errorlog = '-'
accesslog = '-'
capture_output = True

bind = ['0.0.0.0:5000']
max_requests = 10000
max_requests_jitter = 1000

workers = int(os.getenv('GUNICORN_WORKERS'))
worker_class = os.getenv('GUNICORN_WORKER_CLASS')
