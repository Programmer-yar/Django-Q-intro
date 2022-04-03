from time import sleep
from django.conf import settings
import os

def sleep_and_print(secs, num):
    print("Hey, we got a num", num)
    sleep(secs)
    print('Wow!! ran the task with Django Q')


# def write_it(text):
#     print(text)
#     with open ('message.txt', 'w') as file:
#         file.write(text)
#     print('ran succesfully')

def print_something(text):
    print(text)
    path = os.path.join(settings.BASE_DIR, 'alert.txt')
    with open(path, 'w') as new_file:
        new_file.write(text)
    print("written")
