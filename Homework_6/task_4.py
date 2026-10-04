import functools


def retry(count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, count + 1):
                print(f"Попытка {attempt}")
                result = func(*args, **kwargs)
                if result is True:
                    return True
            return False

        return wrapper

    return decorator


counter = 0


@retry(6)
def test():
    global counter
    counter += 1
    return counter >= 5


print("Итог:", test())

counter_2 = 0


@retry(2)
def test_2():
    global counter_2
    counter_2 += 1
    return counter_2 >= 3


print("Итог:", test_2())
