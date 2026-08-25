def safe(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return None

    return wrapper


@safe
def divide(a, b):
    return a / b


print(divide(10, 0))#10/0　is not able to caluculate in Math