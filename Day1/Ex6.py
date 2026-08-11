d1 = {'a': 10, 'b': 5}
d2 = {'a': 5, 'c': 1}

merged = {}

for key in d1.keys() | d2.keys():
    merged[key] = d1.get(key, 0) + d2.get(key, 0)

print(merged)