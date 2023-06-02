from celery import Celery
from celery.utils.log import get_task_logger
import config
import time
logger = get_task_logger(__name__)

celery_app = Celery('celery_tasks', broker=config.REDIS_BROKER, backend=config.REDIS_BACKEND)
@celery_app.task(name = 'first_celery')
def add(x,y):
    time.sleep(30)
    print(x+y)