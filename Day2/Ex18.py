def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Original result: {result}")

        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(1, 2))