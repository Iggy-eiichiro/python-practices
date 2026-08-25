import time
def logger(func):#usef to track events, errors, amd data during program execution
    def wrapper(*args, **kwargs):
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")

        return func(*args, **kwargs)

    return wrapper


@logger
def func(x, y, a=0):
    return x + y + a

start = time.time()
result=func(1, 2, a=3)
end= time.time()
print(f"time: {end-start:.5f}s")