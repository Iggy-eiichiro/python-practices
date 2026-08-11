numbers = [[1, 2], [3, 4], [5]]
flattened = []
for subulist in numbers:
    for number in subulist:
        flattened.append(number)
print(flattened)