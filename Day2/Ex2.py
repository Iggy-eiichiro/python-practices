def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Retry {i + 1}")

            print("Failed")
            return None

        return wrapper

    return decorator


@retry(3)
def connect():
    raise ConnectionError("Connection failed")


connect()

