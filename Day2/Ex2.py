def retry(n):
    def decorator(func):# decorator is a function that tskes another function as an argument.
        def wrapper(*args, **kwargs):
            for i in range(n):
                try:# when error has possibility to be happened, do this process
                    return func(*args, **kwargs)
                except Exception:# when error already happened, do this process
                    print(f"Retry {i + 1}")

            print("Failed")
            return None# many times failed, it's mean there is no success

        return wrapper# order to use wrapper

    return decorator# order to use decorator


@retry(3)
def connect():
    raise ConnectionError("Connection failed")# on porpose, make it error, because for education


connect()

