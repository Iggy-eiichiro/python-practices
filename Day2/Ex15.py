import time
 
timer_done = False
logger_done = False

def timer(func):
    def wrapper(*args, **kwargs):
        global timer_done# global, it makes timer_done(variable) usuable in the block, similar to nonlocal

        start = time.time()
        results = func(*args, **kwargs)
        end = time.time()

        print(f"Time: {end - start:.2f}s")
        timer_done = True
        return results
    
    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        global logger_done
        

        print(f"Args: {args}, Kwargs: {kwargs}")
        
        logger_done = True
        return func(*args, **kwargs)
    return wrapper


@timer
@logger
def add(a, b):
    return a + b


print(add(1, 2))
if timer_done and logger_done:
    print("Both logs the parameters and prints the execution time.")
 
 