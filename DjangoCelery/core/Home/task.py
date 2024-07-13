# Create your tasks here

from celery import shared_task
import time

@shared_task
def WaitingTime():
    print("Task is Running")
    time.sleep(20)