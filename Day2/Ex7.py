import time

def rate_limit(n, seconds):
    calls = []

    def decorator(func):
        def wrapper(*args, **kwargs):
            now = time.time()#it express how much time has passed since

            calls[:] = [
                t for t in calls
                if now - t < seconds # assuming now is 2s,t is 0.7s. it's been 1.3s since i called hello()
            ] # first of t, take the t and put in the list.# for t  in calls, take from calls 1 by 1 and put in t.

            if len(calls) >= n: 
                print("Too many requests")
                return None

            calls.append(now)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limit(2, 1)
def hello():
    print("Hello")
     
hello()
hello()
hello()
hello()
hello()
hello()
hello()
hello()
hello()
hello()
