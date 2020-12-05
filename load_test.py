from random import choice, randint
import asyncio
import string
from aiohttp import ClientSession


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(choice(letters) for i in range(length))
    return result_str


async def fetch(url, session):
    async with session.get(url) as response:
        delay = response.headers.get("DELAY")
        date = response.headers.get("DATE")
        print("{}:{} with delay {}".format(date, response.url, delay))
        return await response.read()


async def bound_fetch(sem, url, session):
    # Getter function with semaphore.
    async with sem:
        await fetch(url, session)


async def run(r, url):
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(1000)

    # Create client session that will ensure we dont open new connection
    # per each request.
    async with ClientSession() as session:
        for i in range(r):
            # pass Semaphore and session to every GET request
            task = asyncio.ensure_future(bound_fetch(sem, url.format(i), session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses

while True:
    number_root = randint(0, 3000)
    url_root = "http://localhost:5000"
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(number_root, url_root))
    loop.run_until_complete(future)
    
    number_ip = randint(0, 500)
    url_ip = "http://localhost:5000/ip"
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(number_ip, url_ip))
    loop.run_until_complete(future)
    
    number_error = randint(0, 500)
    url_error = "http://localhost:5000/error"
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(number_error, url_error))
    loop.run_until_complete(future)

    number_non_existent = randint(0, 100)
    url_non_existent = f'http://localhost:5000/{get_random_string(8)}'
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(number_non_existent, url_non_existent))
    loop.run_until_complete(future)
