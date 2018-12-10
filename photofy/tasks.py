from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time

@shared_task(name = "periodic")
def print_periodic():
  print('periodic whaeee!!!')


@shared_task(name = "print_msg_with_name")
def print_message(name, *args, **kwargs):
  print("Celery is working!! {} have implemented it correctly.".format(name))

@shared_task(name = "add_2_numbers")
def add(x, y):
  time.sleep(20)
  print("Add function has been called!! with params {}, {}".format(x, y))
  return x+y

@shared_task(name = 'download data')
def download_data(link):
  # getting all video links
  print('consuming resources')
  time.sleep(30)
