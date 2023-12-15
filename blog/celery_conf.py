from celery import Celery


celery_app = Celery('blog', broker='redis://redis:6379/0')

# Загружаем сеттинги из джанги
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживает и регистрирует задачи из всех файлов tasks.py
celery_app.autodiscover_tasks()
