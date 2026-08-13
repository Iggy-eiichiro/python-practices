import time

def delay(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@delay(3)
def hello():
    print("Hello")

start = time.perf_counter()
results = hello()
end = time.perf_counter()

print(results)
print(f"time:{end-start:.2f}s")