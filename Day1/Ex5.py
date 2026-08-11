numbers = [1, [2, [3, 4]], 5]
flattened = []

def flatten_list(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            flatten_list(item)
        else:
            flattened.append(item)


print(flattened)