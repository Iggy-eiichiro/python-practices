def add_doc(text):
    def decorator(func):
        func.__doc__ = (func.__doc__ or "") + "\n" + text# (or "") is mean, if (func.__doc__ )is emoty.("\n") is line break
        return func

    return decorator


@add_doc("This function adds two numbers.")
def add(a, b):
    """Original documentation."""

    return a + b


help(add)