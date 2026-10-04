import functools


def log_test(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Название теста: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} выполнен")
        print(f"Результат: {result}")
        return result

    return wrapper


@log_test
def test(a, b):
    return a * b


test(5, 5)
