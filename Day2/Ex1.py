import time

def timer(func):# func is a reusable block of organized code designed to perform a single, specific task
    def wrapper(*args,**kwargs):# wrapper is a design pattern that allows to modify or extend the behavior of function, method, or class without permanently changing its core code.
        start_time = time.time()#time() is a function in the built in time module that returns the current itime as a floating-point number.

        result = func(*args,**kwargs)# test(): time..sleep(1) is going to come here later.

        end = time.time()
        print(f"Time:{ end - start_time:.2f}s")#print(f"Time:{ end - start_time:.2f}s") of f, if there is, inside of {} is to be changed.

        return result
    return wrapper

@ timer
def test():
    time.sleep(1)#sleep() is a function that pauses your cod for a set amount of time

test()