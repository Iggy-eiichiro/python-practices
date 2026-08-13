registry = []


def register(func):
    registry.append(func)
    return func# bakc to each function as it is.


@register
def function_a():
    pass


@register
def function_b():
    pass


@register
def function_c():
    pass


print(registry)
for func in registry:
    print(func.__name__)