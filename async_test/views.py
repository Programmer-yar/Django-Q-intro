import asyncio
from asgiref.sync import sync_to_async

from django.shortcuts import render
from django.http import JsonResponse
from time import sleep

from django_q.tasks import async_task


def test(request):
    json_payload = {
        'message': 'hello World'
    }
    sleep(10)

    return JsonResponse(json_payload)


@sync_to_async
def crunching_stuff():
    sleep(10)
    print("Woke Up after 10 seconds")


async def index(request):
    json_payload = {
        'message': 'hello man, this is async'
    }

    asyncio.create_task(crunching_stuff())
    return JsonResponse(json_payload)


def with_django_q(request):
    json_payload = {
        'message': 'hellooo django Q...!!'
    }

    #'async_task' is a principle Django Q function
    #First arg is path to function and second one consists of args that
    #called function takes
    message = "Always believe in yourself!"
    # async_task("async_test.services.write_it", message)
    async_task("async_test.services.print_something", message)
    async_task("async_test.services.sleep_and_print", 10, 11)
    return JsonResponse(json_payload)