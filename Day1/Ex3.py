numbers = [3, 1, 2, 3, 4, 1]
squared = []

for number in dict.fromkeys(numbers): # dict.fromkeys(), dictionary is able to hold only one key, so due to use the function, cleanly erase duplication
    squared.append(number)

print(squared)

