import time
def memoize(func):
    cache = {}# cache is a temporary storage location for data 

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)

        return cache[n]

    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:#the number start from 35, so n = 0 is mean finish the calculate
        return n# when new number shows up, as the same time,n get the number. it's mean when fibonacci(33) shows up,then 33 go to n.

    return fibonacci(n - 1) + fibonacci(n - 2)

start = time.perf_counter()
result =fibonacci(35)
end = time.perf_counter()

print(result)
print(f"Time:{end - start:.5f}s")

# without @memoize
# 9227465                                                                                                   
# Time:2.19481s

#with @memoize
# 9227465
# Time:0.00004s
