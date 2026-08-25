numbers = [1, 2]
letters = ['a', 'b']

result = []
for i in range(len(numbers)):# i is the index of the first list, which is numbers
    result.append((numbers[i], letters[i]))

print(result)