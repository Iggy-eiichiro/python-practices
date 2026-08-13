def deprecated(func):#func get "old_function()"
    def wrapper(*args, **kwargs):
        print(f"Warning: Function {func.__name__} is deprecated")#{func.__name__} execute print("Old function")
        return func(*args, **kwargs)

    return wrapper


@deprecated
def old_function():
    print("Old function")


old_function()