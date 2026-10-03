import os

bind = os.environ.get("GUNICORN_BIND", "0.0.0.0:8000")
# SQLite admite una sola escritura a la vez; pocos workers evitan "database is locked"
workers = int(os.environ.get("WEB_CONCURRENCY", 3))
worker_class = "sync"
max_requests = 1000
max_requests_jitter = 50
timeout = 30
keepalive = 2
