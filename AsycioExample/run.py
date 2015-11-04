# PYTHON 3.5 ASYNCIO EXAMPLE
import asyncio
import random
import time


_TASK_NUM = 20
_WAIT_LOW = 0
_WAIT_HIGH = 2


# --------------------- ASYNC ------------------------------------
async def a_compute(x, y):
    await asyncio.sleep(random.randint(_WAIT_LOW, _WAIT_HIGH))
    return x + y


async def a_print_sum(x, y):
    result = await a_compute(x, y)
    print("%s + %s = %s" % (x, y, result))


def async():
    loop = asyncio.get_event_loop()
    tasks = []

    for i in range(_TASK_NUM):
        task = a_print_sum(random.randint(1, 10), random.randint(1, 10))
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
# --------------------------------------------------------------


# ~~~~~~~~~~~~~~~~~~~~~~~~~ SYNC  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def compute(x, y):
    time.sleep(random.randint(_WAIT_LOW, _WAIT_HIGH))
    return x + y


def print_sum(x, y):
    result = compute(x, y)
    print("%s + %s = %s" % (x, y, result))


def sync():
    for i in range(_TASK_NUM):
        print_sum(random.randint(1, 10), random.randint(1, 10))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def main():
    a_start = time.time()
    async()
    a_end = time.time()
    print("Async took: ", a_end - a_start)

    s_start = time.time()
    sync()
    s_end = time.time()
    print("SYNC took: ", s_end - s_start)


if __name__ == '__main__':
    main()
