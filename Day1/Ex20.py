data = {'a':1,'b':2}
results = {}

for key, value in data.items():#items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
    results[value] = key# swap the key and value, so the value becones the key, and the key becomes the value.
print(results)# if tab in the for loop, output is 2 times, because the key is unique, but the value is not unique. key can not be repeated, but vale can be repeated.
