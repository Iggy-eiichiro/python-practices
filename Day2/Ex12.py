def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, (int, float))：# kinda if type
            return result * 2

        return result

    return wrapper


@double_result
def get_number():
    return 5


print(get_number())