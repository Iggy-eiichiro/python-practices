data = [{'val': 10}, {'val': 50}]

result = max(item['val'] for item in data)#'val'of value is the key, key is for finding the maximum value in the list of dictionaries.

print(result)