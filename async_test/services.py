from time import sleep

def sleep_and_print(secs, num):
    print("Hey, we got a num", num)
    sleep(secs)
    print('Wow!! ran the task with Django Q')


def write_it(text):
    with open ('message.txt', 'w') as file:
        file.write(text)
    print('ran succesfully')
