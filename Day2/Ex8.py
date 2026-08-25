import json

def json_formatter(func):# make json type
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapper


@json_formatter
def get_user():
    return {
        'name': 'Tom',
        'age': 20
    }


print(get_user())#if the answer would be doule quotation, which mean json type