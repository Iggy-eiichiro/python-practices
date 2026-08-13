import os
os.environ["DEBUG"]= "True"
def debug(func):
    def wrapper(*args, **kwargs):

        if os.getenv("DEBUG") == "True":
            print(f"DEBUG: args={args}, kwargs={kwargs}")

        return func(*args, **kwargs)

    return wrapper


@debug
def add(a, b):
    return a + b


add(1, 2)